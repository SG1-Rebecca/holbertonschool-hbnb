from flask_restx import Namespace, Resource, fields
from app.services import facade


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

        existing_user = facade.get_user_by_email(user_data.get('email', ''))
        if existing_user:
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

        @api.expect(user_model, validate=True)
        @api.response(200, 'OK')
        @api.response(404, 'Not Found')
        @api.response(400, 'Bad Request')
        def put(self, user_id):
            """Update user details by ID"""
            user_data = api.payload

            try:
                update_user = facade.update_user(user_id, user_data)
                if not update_user:
                    return {'error': 'Not Found'}, 404
                return update_user.to_dict_public(), 200
            except Exception as e:
                return {'error': str(e)}, 400
