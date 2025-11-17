from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade
from app import bcrypt

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        
        user_data['password'] = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')

        try:
            new_user = facade.create_user(user_data)
            return {'id': new_user.id, 'message': 'User successfully created'}, 201

        except Exception as error:
            return {'error': str(error)}, 400

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Get the lists of users"""
        user_list = facade.get_all_users()
        return [user.to_dict() for user in user_list], 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User details updated successfully')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    @api.response(400, 'You cannot modify email or password')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def put(self, user_id):
        """Update a user"""
        current_user = get_jwt_identity()
        user_data = api.payload

        if user_id != current_user:
            return {'error': 'Unauthorized action'}, 403
        
        if 'email' in user_data:
            return {'error': 'You cannot modify email'}, 400
        
        if 'password' in user_data:
            return {'error': 'You cannot modify password'}, 400

        try:
            updated_user = facade.update_user(user_id, user_data)
            if not updated_user:
                return {'error': 'User not found'}, 404
            return updated_user.to_dict(), 200

        except Exception as error:
            return {'error': str(error)}, 400
