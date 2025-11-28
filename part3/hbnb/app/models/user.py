from app import bcrypt, db
from app.models.base_model import BaseModel
from sqlalchemy.orm import validates
import re


class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


    def __init__(self, first_name: str, last_name: str, email: str, password: str, is_admin: bool =False):
        """
        Initialize a User instance with email, password, first name, last name,
        and admin status.

        Args:
            email (str): The user's email address.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            is_admin (bool): Indicates if the user has admin privileges.
                            Default to False.
        """
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.hash_password(password)
        self.is_admin = is_admin


    @validates("first_name", "last_name")
    def validate_names(self, key, value):
        """
        Validate first_name and last_name.
        """
        if not isinstance(value, str):
            raise TypeError(f"The {key} must be an string")

        if not value.strip():
            raise ValueError(f"The {key} must be a non-empty string")

        if len(value.strip()) > 50:
            raise ValueError(f"The {key} must have a maximum length of 50 characters")
        return value.strip()

    @validates("email")
    def validate_email(self, key, value):
        """
        Validate email format.
        """
        pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
        if not isinstance(value, str):
            raise TypeError(f"{key} must be a string")

        if not value.strip():
            raise ValueError(f"{key} must be a non-empty string")

        if not re.match(pattern, value.strip()):
            raise ValueError("Invalid email format")
        return value.strip()
    
    def verify_password(self, password):
        """
        Verifies if the provided password matches the hashed password.
        """
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        return bcrypt.check_password_hash(self.password, password)

    def hash_password(self, password):
        """
        Hashes the password before storing it.
        """
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    @validates("is_admin")
    def validate_admin(self, key, value):
        """
        Validate admin status.
        """
        if not isinstance(value, bool):
            raise TypeError("is_admin must be a boolean")
        return value

    def add_place(self, place):
        """
        Add an amenity to the place.
        """
        self.places.append(place)

    def add_review(self, review):
        """
        Add an amenity to the place.
        """
        self.reviews.append(review)

    def delete_review(self, review):
        """
        Add an amenity to the place.
        """
        self.reviews.remove(review)

    def to_dict(self):
        """
        Convert the User instance to a dictionary.
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
