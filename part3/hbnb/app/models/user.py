from app.models.base_model import BaseModel
from email_validator import validate_email, EmailNotValidError
from app import bcrypt


class User(BaseModel):
    """
    User model that inherits from BaseModel
    """
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """
        Initialize new user instance

        Args:
            first_name (str): The user's first name
            last_name (str): The user's last name
            email (str): The user's email address
            password (str): The user's password
            is_admin (bool): User admin status, defaults to False
        """
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hash_password(password)  # hash the password before storing
        self.is_admin = is_admin

    @property
    def first_name(self):
        """
        Get the user's first name

        Returns:
            str: The user's first name
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        """
        Set the user's first name

        Args:
            value (str): The first name to set

        Raises:
            ValueError: If value is not a non-empty string
                        or exceeds 50 characters
        """
        if not isinstance(value, str) or not value:
            raise ValueError("first_name must be a non-empty string")

        if len(value) > 50:
            raise ValueError("first_name must not exceed 50 characters")
        self.__first_name = value.strip()

    @property
    def last_name(self):
        """
        Get the last name

        Returns:
            str: Last name
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """
        Set last name

        Args:
            value (str): Last name
        """
        if not isinstance(value, str) or not value:
            raise ValueError("last_name must be a non-empty string")
        if len(value) > 50:
            raise ValueError("last_name must be less than 50 characters")
        self.__last_name = value.strip()

    @property
    def email(self):
        """
        Get the user's email address

        Returns:
            str: The normalized email address
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        Set the user's email address
        The email is validated and normalized using email_validator

        Args:
            value (str): The email address to set

        Raises:
            ValueError: If the email is empty, not a string,
            or has an invalid format
        """
        if not isinstance(value, str):
            raise TypeError("Email must be a string")

        value = value.strip()

        if not value:
            raise ValueError("Email cannot be empty")

        try:
            email_info = validate_email(value, check_deliverability=False)
            self.__email = email_info.normalized
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

    @property
    def is_admin(self):
        """
        Check if user is admin

        Returns:
            bool: True if admin, False otherwise
        """
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value):
        """
        Set user's admin status

        Args:
            value (bool): Admin status

        Raises:
            ValueError: If value not a boolean
        """
        if not isinstance(value, bool):
            raise ValueError("is_admin must be a boolean value")
        self.__is_admin = value

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
