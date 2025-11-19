from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from app.services import facade

api = Namespace('admin', description='Admin operations')

# Models for request validation
user_model = api.model('User', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=False, description='User password'),
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'is_admin': fields.Boolean(required=False, description='Admin status')
})

user_update_model = api.model('UserUpdate', {
    'email': fields.String(required=False, description='User email'),
    'password': fields.String(required=False, description='User password'),
    'first_name': fields.String(required=False, description='First name'),
    'last_name': fields.String(required=False, description='Last name'),
    'is_admin': fields.Boolean(required=False, description='Admin status')
})

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Amenity name')
})

@api.route('/users/<user_id>')
class AdminUserResource(Resource):
    @api.response
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt()

        user_data = api.payload
        
        # If 'is_admin' is part of the identity payload
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        data = request.json
        email = data.get('email')

        if email:
            # Check if email is already in use
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400

        # Logic to update user details, including email and password

@api.route('/users/')
class AdminUserCreate(Resource):
    @api.expect(user_model)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Admin privileges required')
    @api.response(404, 'User not found')
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json
        email = user_data.get('email')

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        # Logic to create a new user
        try:
            user = facade.create_user(user_data)
            return user.to_dict(), 201
        except ValueError:
            return {'error': 'Email already registered'}, 400
        except Exception as error:
            return {'error': str(error)}, 400

@api.route('/users/<user_id>')
class AdminUserModify(Resource):
    @api.expect(user_update_model)
    @api.response(201, 'User successfully updated')
    @api.response(403, 'Admin privileges required')
    @api.response(400, 'Email already in use')
    @api.response(404, 'User not found')
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
            
        user_to_update = facade.get_user(user_id)
        if not user_to_update:
            return {'error': 'User not found'}, 404

        # Logic to update user details
        try:
            updated_user = facade.update_user(user_id, data)
            if updated_user:
                return updated_user.to_dict(), 201

@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        # Logic to create a new amenity
        pass

@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        # Logic to update an amenity
        pass