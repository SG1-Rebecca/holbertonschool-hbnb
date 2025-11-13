from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(400, 'You cannot review your own place')
    @api.response(400, 'You have already reviewed this place')
    @jwt_required()
    def post(self):
        """Register a new review"""
        current_user = get_jwt_identity()
        review_data = api.payload

        review_data['user_id'] = current_user

        place = facade.get_place(review_data['place_id'])
        if not place:
            return {'error': 'Place not found'}, 400
        
        if place.owner_id == current_user:
            return {'error': 'You cannot review your own place'}, 400
        
        review_exists = facade.get_review_user_place(current_user, review_data['place_id'])
        if review_exists:
            return {'error': 'You have already reviewed this place'}

        try:
            new_review = facade.create_review(review_data)
            return new_review.to_dict(), 201
        except Exception as error:
            return {'error': str(error)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return [], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return review.to_dict(), 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def put(self, review_id):
        """Update a review's information"""
        current_user = get_jwt_identity()
        review_data = api.payload

        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404

        if review['user_id'] != current_user:
            return {'error': 'Unauthorized action'}, 403

        try:
            review_data['user_id'] = current_user

            updated_review = facade.update_review(review_id, review_data)
            return updated_review.to_dict(), 200

        except Exception as error:
            return {'error': str(error)}, 400

    @api.response(200, 'Review deleted successfully')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'Review not found')
    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404
        
        if review['user_id'] != current_user:
            return {'error': 'Unauthorized action'}, 403
            
        try:
            facade.delete_review(review_id)
            return {'message': 'Review deleted successfully'}, 200
        except Exception as error:
            return {'error': str(error)}, 400