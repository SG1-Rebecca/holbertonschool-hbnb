from base_model import BaseModel
from place import Place
from user import User

class Review(BaseModel):
    """
    """
    MIN_RATING = 1
    MAX_RATING = 5
    def __init__(self, text, rating, place, user):
        """
        Initialize a Review instance.

        Args:
            text (str):
            rating (int): 
            place (Place)
            user (User)
        """
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    def validate_text(self):
        """
        Validate the format of the review text
        """
        if not isinstance(self.text, str):
            raise ValueError("Text must be a string")

        if not self.text.strip():
            raise ValueError("Text cannot be empty")

    def validate_rating(self):
        """
        Validate the format and rating of the review
        """
        if not isinstance(self.rating, int) or self.rating < self.MIN_RATING or self.rating > self.MAX_RATING:
            raise ValueError(f"Rating must be an integer between {self.MIN_RATING} and {self.MAX_RATING}")

    def validate_place(self):
        """
        Check if place is a Place instance.
        """
        if not isinstance(self.place, Place):
            raise ValueError("place must be a valid instance of Place")

    def validate_user(self):
        """
        Check if user is a User instance.
        """
        if not isinstance(self.user, User):
            raise ValueError("user must be a valid instance of User")