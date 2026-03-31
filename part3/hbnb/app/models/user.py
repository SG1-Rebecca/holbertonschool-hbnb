from app import db, bcrypt
import uuid
from app.models.base_model import BaseModel
from email_validator import validate_email, EmailNotValidError
from sqlalchemy.orm import validates, relationship


class User(BaseModel):
    """
    User model that inherits from BaseModel
    """
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Relationships
    places = relationship('Place', backref='owner', lazy=True)
    reviews = relationship('Review', backref='user', lazy=True)

    @validates('email')
    def validate_user_email(self, key, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string")

        value = value.strip()

        if not value:
            raise ValueError("Email cannot be empty")

        try:
            email_info = validate_email(value, check_deliverability=False)
            return email_info.normalized
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email format: {str(e)}")

    def hash_password(self, password):
        """
        Hashes the provided password using bcrypt and stores it.

        Args:
            password (str): The plaintext password to hash
        """
        if not isinstance(password, str) or not password:
            raise ValueError("Password must be a non-empty string")

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """
        Verifies if the provided password matches the hashed password.

        Args:
            password (str): The plaintext password to verify

        Returns:
            bool: True if the password matches, False otherwise
        """
        return bcrypt.check_password_hash(self.password, password)


    def to_dict(self):
        """
        Convert user instance into a dictionary

        Returns:
            dict: Dictionary representation of user
        """
        user_dict = super().to_dict()
        user_dict.update({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        })
        return user_dict

    def to_dict_public(self):
        """
        Return a public dictionary representation of the user,
        excluding timestamps
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
