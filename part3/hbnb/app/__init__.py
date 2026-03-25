import os
from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

load_dotenv()

bcrypt = Bcrypt()
jwt = JWTManager()

authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Bearer token'
    }
}

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/', authorizations=authorizations, security='Bearer')

    # Initialize extensions
    bcrypt.init_app(app)
    jwt.init_app(app)

    # To avoid circular imports, we import the namespaces here after initializing the app and extensions
    from app.api.v1.users import api as users_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.reviews import api as reviews_ns
    from app.api.v1.auth import api as auth_ns

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(auth_ns, path='/api/v1/auth')

    with app.app_context():
        from app.services import facade
        admin_email = os.getenv('ADMIN_EMAIL')
        admin_password = os.getenv('ADMIN_PASSWORD')

        if admin_email and admin_password:
            if not facade.get_user_by_email(admin_email):
                facade.create_user({
                    'first_name': 'Admin',
                    'last_name': 'User',
                    'email': admin_email,
                    'password': admin_password,
                    'is_admin': True
                })

    return app
