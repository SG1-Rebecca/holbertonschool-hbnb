from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt
from app.services import facade

api = Namespace('admin', description='Admin operations')


@api.route('/users/')
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json
        email = user_data.get('email')

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400
        
        # Logic to create a new user
        try:
            create_new_user = facade.create_user(user_data)
            return {'id': create_new_user.id, 'message': 'Admin created user successfully'}, 201
        except Exception as error:
            return {'error': str(error)}, 400
        


@api.route('/users/<user_id>')
class AdminUserModify(Resource):
    @api.response(200, 'User successfully updated by admin')
    @api.response(400, 'User successfully updated by admin')
    @api.response(403, 'Admin privileges required')
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        data = request.json
        email = data.get('email')

        # Ensure email uniqueness
        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already in use'}, 400

        # Logic to update user details, including email and password
        try:
            facade.update_user(user_id, data)
            return {'message': 'User successfully updated by admin'}, 200
        except Exception as error:
            return {'error': str(error)}, 400


@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        amenity_data = request.json

        # Logic to create a new amenity
        try:
            new_amenity = facade.create_amenity(amenity_data)
            return {'id': new_amenity.id, 'name': new_amenity.name}, 201
        except Exception as error:
            return {'error': str(error)}, 400


@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        amenity_data = request.json

        # Logic to update an amenity
        try:
            updated_amenity = facade.update_amenity(amenity_id, amenity_data)
            return {'name': updated_amenity.name}, 200
        except Exception as error:
            return {'error': str(error)}, 400


@api.route('/places/<place_id>')
class AdminPlaceModify(Resource):
    @jwt_required()
    def put(self, place_id):
        current_user = get_jwt()

        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('id')

        place = facade.get_place(place_id)
        if not is_admin and place.owner_id != user_id:
            return {'error': 'Unauthorized action'}, 403

        place_data = request.json

        # Logic to update the place
        try:
            facade.update_place(place_id, place_data)
            return {'message': 'Place updated successfully by admin'}, 200
        except Exception as error:
            return {'error': str(error)}, 400
