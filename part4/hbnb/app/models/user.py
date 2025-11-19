from app.models.base_model import BaseModel
from app import bcrypt
import re


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """

    def __init__(self, email, first_name, last_name, password, is_admin=False):
        """
        Initialize a User instance with email, password, first name, last name,
        and admin status.

        Args:
            email (str): The user's email address.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            password (str): The user's password.
            is_admin (bool): Indicates if the user has admin privileges.
                            Default to False.
        """
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
        self.hash_password(password)

    @property
    def email(self):
        """
        Get the email adress
        """
        return self.__email
    
    @email.setter
    def email(self, value):
        """
        Set the email address
        """
        pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
        if not isinstance(value, str):
            raise TypeError("Email must be a string")

        if not value.strip():
            raise ValueError("Email must be a non-empty string")

        if not re.match(pattern, value.strip()):
            raise ValueError("Invalid email format")
        self.__email = value.strip()

    @property
    def first_name(self):
        """
        Get the first name
        """
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value):
        """
        Set and validate the first name
        """
        if not isinstance(value, str):
            raise TypeError("The first name must be a string")

        if not value.strip():
            raise ValueError("The first name must be a non-empty string")

        if len(value.strip()) > 50:
            raise ValueError("The first name must have a maximum length of 50 characters")
        self.__first_name = value.strip()

    @property
    def last_name(self):
        """
        Get the last name
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """
        Set and validate the last name
        """
        if not isinstance(value, str):
            raise TypeError("The last name must be a string")

        if not value.strip():
            raise ValueError("The last name must be a non-empty string")

        if len(value.strip()) > 50:
            raise ValueError("The last name must have a maximum length of 50 characters")
        self.__last_name = value.strip()
    
    def hash_password(self, password):
        """
        Hashes the password before storing it.
        """
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        if not password.strip():
            raise ValueError("Password cannot be empty")
        self.__password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def verify_password(self, password):
        """
        Verifies if the provided password matches the hashed password.
        """
        return bcrypt.check_password_hash(self.__password, password)

    @property
    def is_admin(self):
        """
        Get the admin status
        """
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value):
        """
        Set and validate the admin status
        """
        if not isinstance(value, bool):
            raise TypeError("is_admin must be a boolean")
        self.__is_admin = value

    def to_dict(self):
        """
        Convert the User instance to a dictionary.
        """
        user_dict = super().to_dict()
        user_dict.update({
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        })
        return user_dict
