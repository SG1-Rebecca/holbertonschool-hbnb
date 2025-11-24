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
    @api.response(400, 'User not found')
    @api.response(400, 'Place not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new review"""
        review_data = api.payload
        current_user = get_jwt_identity()

        place = facade.get_place(review_data.get('place_id'))
        if not place:
            return {'error': 'Place not found'}, 400

        if place.owner_id == current_user:
            return {'You cannot review your own place'}, 400

        if facade.user_reviewed(current_user, review_data.get('place_id')):
            return {'error': 'User already reviewed this place'}, 400

        review_data['user_id'] = current_user

        try:
            new_review = facade.create_review(review_data)
            return new_review.to_dict(), 201
        except Exception as error:
            return {'error': str(error)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return [review.to_dict() for review in reviews], 200

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
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'Review not found')
    @jwt_required()
    def put(self, review_id):
        review_data = api.payload
        current_user = get_jwt_identity()

        review_update = facade.get_review(review_id)
        if not review_update:
            return {'Review not found'}, 404

        if review_update.user_id != current_user:
            return {'Unauthorized action'}, 403

        try:
            updated_review = facade.update_review(review_id, review_data)
            if not updated_review:
                return {'error': 'Review not found'}, 404
            return updated_review.to_dict(), 200
        except Exception as error:
            return {'error': str(error)}, 400

    @api.response(200, 'Review deleted successfully')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'Review not found')
    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        review = facade.get_review(review_id)
        current_user = get_jwt_identity()

        if not review:
            return {'error': 'Review not found'}, 404
        
        if review.user_id != current_user:
            return {'Unauthorized action'}, 403

        try:
            facade.delete_review(review_id)
            return {'message': 'Review deleted successfully'}, 200
        except Exception as error:
            return {'error': str(error)}, 400
