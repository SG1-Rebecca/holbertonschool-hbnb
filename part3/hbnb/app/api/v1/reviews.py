from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

review_update_model = api.model('ReviewUpdate', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
})


@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new review"""
        current_user = get_jwt_identity()

        review_data = api.payload

        place = facade.get_place(review_data['place_id'])
        if not place:
            return {'error': 'Place not found'}, 400

        # Override any user_id provided in the request to prevent impersonation
        review_data['user_id'] = current_user

        if place.owner.id == current_user:
            return {'error': 'You cannot review your own place'}, 400

        # Check that the user has not already reviewed this place.
        existing_review = facade.get_reviews_by_place(review_data['place_id'])

        if any(review.user.id == current_user for review in existing_review):
            return {'error': 'You have already reviewed this place.'}, 400

        try:
            new_review = facade.create_review(review_data)
            return new_review.to_dict_public(), 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        review_list = facade.get_all_reviews()
        return [review.to_dict_list() for review in review_list], 200


@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404
        return review.to_dict_public(), 200

    @api.expect(review_update_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, review_id):
        """Update a review's information"""
        current_user = get_jwt()

        review_data = api.payload

        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('sub')

        print(f"Debug - User ID: {user_id}, Is Admin: {is_admin}")

        # Check that the user_id of the review matches the authenticated user.
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 400

        if not is_admin and review.user.id != user_id:
            return {'error': 'Unauthorized action.'}, 403

        try:
            update_review = facade.update_review(review_id, review_data)
            if not update_review:
                return {'error': 'Review not found'}, 404
            return update_review.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        current_user = get_jwt()

        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('sub')

        print(f"Debug - User ID: {user_id}, Is Admin: {is_admin}")

        review = facade.get_review(review_id)


        # Check that the user_id of the review matches the authenticated user.
        if not is_admin and review.user.id != user_id:
            return {'error': 'Unauthorized action.'}, 403

        try:
            facade.delete_review(review_id)
            return {'message': 'Review deleted successfully'}, 200
        except ValueError as e:
            return {'error': str(e)}, 404
