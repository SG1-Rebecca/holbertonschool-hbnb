from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')
    bcrypt.init_app(app)

    from app.api.v1.users import api as users_ns

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    return app