from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

# Define the user update model for input validation and documentation
user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new user"""
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = api.payload
        email = user_data.get('email')

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
        except (ValueError, TypeError) as e:
            return {'error': str(e)}, 400

        return {'id': new_user.id}, 201

    @api.response(200, 'OK')
    def get(self):
        """Retrieve a list of users"""
        users_list = facade.get_all_users()
        return [user.to_dict() for user in users_list], 200

    @api.route('/<user_id>')
    class UserResource(Resource):
        @api.response(200, 'User details retrieved successfully')
        @api.response(404, 'User not found')
        def get(self, user_id):
            """Get user details by ID"""
            user = facade.get_user(user_id)
            if not user:
                return {'error': 'User not found'}, 404
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }, 200

        @api.expect(user_update_model, validate=True)
        @api.response(200, 'OK')
        @api.response(404, 'Not Found')
        @api.response(400, 'Bad Request')
        @jwt_required()
        def put(self, user_id):
            """Update user details by ID"""
            current_user = get_jwt()

            if not current_user.get('is_admin'):
                return {'error': 'Admin privileges required'}, 403

            user_data = api.payload
            email = user_data.get('email')

            # Ensure email uniqueness
            if email:
                existing_user = facade.get_user_by_email(email)
                if existing_user and existing_user.id != user_id:
                    return {'error': 'Email already in use'}, 400

            try:
                update_user = facade.update_user(user_id, user_data)
                if not update_user:
                    return {'error': 'Not Found'}, 404
                return update_user.to_dict_public(), 200
            except Exception as e:
                return {'error': str(e)}, 400
