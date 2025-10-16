from base_model import BaseModel


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

    def validate_name(self):
        """
        """
        if not isinstance(self.first_name, str):
            raise TypeError("The first name must be an string")

        if len(self.first_name) > 50:
            raise ValueError("The first name must have a maximum length of 50 characters")
        
        if not isinstance(self.last_name, str):
            raise TypeError("The last name must be an string")

        if len(self.last_name) > 50:
            raise ValueError("The last name must have a maximum length of 50 characters")

    def validate_email(self):
        """
        Validate the email format.
        """
        if self.email.count("@") != 1:
            raise ValueError("")
        
        recipient, domain = self.email.split("@")

        if not recipient or not domain:
            raise ValueError("Email must have both recipient and domain parts")
        

