import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()

bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()

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
    # Set up CORS with allowed origins 
    allowed_origins = ['http://127.0.0.1:5000',
                       'http://localhost:5000',
                       'http://127.0.0.1:5500',
                       'http://localhost:5500'
                       ]
    CORS(app, origins=allowed_origins, supports_credentials=True)

    @app.route("/")
    def index():
      return render_template("index.html")

    @app.route("/login")
    def login():
      return render_template("login.html")
    
    @app.route("/place")
    def place():
      place_id = request.args.get('id')
      return render_template("place.html", place_id=place_id)
    
    @app.route("/review")
    def review():
      place_id = request.args.get('id')
      return render_template("add_review.html", place_id=place_id)

    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/', authorizations=authorizations, security='Bearer')

    # Initialize extensions
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

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

    # Create admin user
    with app.app_context():
        from app.models.user import User
        from app.models.place import Place
        from app.models.review import Review
        from app.models.amenity import Amenity
        db.create_all()
        from app.utils.admin import create_admin_user
        create_admin_user()


    return app
