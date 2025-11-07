from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.user import User

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
            place (Place):
            user (User):
        """
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self):
        """
        Validate the format of the review text
        """
        return self.__text
    
    @text.setter
    def text(self, value):
        """
        
        """
        if not isinstance(value, str):
            raise ValueError("Text must be a string")

        if not value.strip():
            raise ValueError("Text cannot be empty")
        self.__text = value

    @property
    def rating(self):
        """
        """
        return self.__rating

    @rating.setter
    def rating(self, value):
        """
        """
        if not isinstance(value, int) or value < self.MIN_RATING or value > self.MAX_RATING:
            raise ValueError(f"Rating must be an integer between {self.MIN_RATING} and {self.MAX_RATING}")
        self.__rating = value

    @property
    def place(self):
        """
        """
        return self.__place
    
    @place.setter
    def place(self, value):
        """
        
        """
        if not isinstance(value, Place):
            raise ValueError("place must be a valid instance of Place")
        self.__place = value

    @property
    def user(self):
        """
        """
        return self.__user
    
    @user.setter
    def user(self, value):
        """
        
        """
        if not isinstance(value, User):
            raise ValueError("user must be a valid instance of User")
        self.__user = value

    def to_dict(self):
        """
        Convert the Review instance to a dictionary.
        """
        review_dict = super().to_dict()
        review_dict.update({
            'text': self.text,
            'rating': self.rating,
            'place_id': getattr(self.place, 'id', None),
            'user_id': getattr(self.user, 'id', None)
        })
        return review_dict
