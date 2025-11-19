from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services import facade
import bcrypt

api = Namespace('auth', description='Authentication operations')

# Model for input validation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload
        print(f"🔐 Login attempt for email: {credentials['email']}")
        
        # Step 1: Retrieve the user based on the provided email
        user = facade.get_user_by_email(credentials['email'])
        print(f"👤 User found: {user is not None}")
        
        if user:
            print(f"📧 User email: {user.email}")
            print(f"🔑 Stored password hash: {user.password}")
            print(f"📝 Provided password: {credentials['password']}")
            
            # Debug: Vérifier le type et la valeur du hash
            print(f"🔍 Type of stored password: {type(user.password)}")
            print(f"🔍 Length of stored password: {len(user.password) if user.password else 'None'}")
            
            # Test de vérification manuelle
            try:
                password_valid = user.verify_password(credentials['password'])
                print(f"✅ Password valid: {password_valid}")
                
                # Test direct avec bcrypt pour debug
                if user.password:
                    direct_check = bcrypt.check_password_hash(user.password.encode('utf-8'), credentials['password'])
                    print(f"🔧 Direct bcrypt check: {direct_check}")
                    
            except Exception as e:
                print(f"❌ Error during password verification: {e}")
        else:
            print(f"❌ No user found with email: {credentials['email']}")
            # Debug: Lister tous les utilisateurs existants
            all_users = facade.get_all_users()
            print(f"📋 All users in system: {[user.email for user in all_users]}")
        
        # Step 2: Check if the user exists and the password is correct
        if not user or not user.verify_password(credentials['password']):
            print(f"🚫 Authentication failed for: {credentials['email']}")
            return {'error': 'Invalid credentials'}, 401

        # Step 3: Create a JWT token with the user's id and is_admin flag
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"is_admin": user.is_admin}
        )
        
        print(f"🎉 Login successful for: {user.email}")
        # Step 4: Return the JWT token to the client
        return {'access_token': access_token}, 200
    
@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        """A protected endpoint that requires a valid JWT token"""
        current_user = get_jwt_identity()
        return {'message': f'Hello, user {current_user}'}, 200