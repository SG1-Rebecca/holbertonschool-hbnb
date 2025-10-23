from app.models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """
    PERMITS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'

    def __init__(self, email, first_name, last_name, is_admin=False):
        """
        Initialize a User instance with email, first name, last name,
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
        Validate the user instance.
        """
        self._validate_name()
        self._validate_email()

    def _validate_name(self):
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

    def _validate_email(self):
        """
        Validate the email format.
        """
        if self.email.count("@") != 1:
            raise ValueError("Email must contain exactly one '@' character")

        recipient, domain = self.email.split("@")

        if not recipient or not domain:
            raise ValueError("Email must have both recipient and domain parts")

        for current_char in recipient:
            if current_char not in self.PERMITS:
                raise ValueError(f"Email recipient contains invalid character: {current_char}")

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
