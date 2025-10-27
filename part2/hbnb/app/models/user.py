from app.models.base_model import BaseModel
import re


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """

    def __init__(self, email, first_name, last_name, is_admin=False):
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
        self.is_admin = is_admin
        self.validate()

    def validate(self):
        """
        Validate the user attributes.
        """
        self.validate_email()
        self.validate_name()

    def validate_name(self):
        """
        Validate the format of the first and last names.
        """
        if not isinstance(self.first_name, str):
            raise TypeError("The first name must be an string")

        if not self.first_name.strip():
            raise ValueError("The first name must be a non-empty string")

        if len(self.first_name.strip()) > 50:
            raise ValueError("The first name must have a maximum length of 50 characters")

        if not isinstance(self.last_name, str):
            raise TypeError("The last name must be an string")

        if not self.last_name.strip():
            raise ValueError("The last name must be a non-empty string")

        if len(self.last_name.strip()) > 50:
            raise ValueError("The last name must have a maximum length of 50 characters")

    def validate_email(self):
        """
        Validate the email format.
        """
        pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
        if not isinstance(self.email, str):
            raise TypeError("Email must be a string")

        if not self.email.strip():
            raise ValueError("Email must be a non-empty string")

        if not re.match(pattern, self.email):
            raise ValueError("Invalid email format")

    def to_dict(self):
        """
        Convert the User instance to a dictionary.
        """
        user_dict = super().to_dict()
        user_dict.update({
            'first_name': self.first_name.strip(),
            'last_name': self.last_name.strip(),
            'email': self.email.strip()
        })
        return user_dict
