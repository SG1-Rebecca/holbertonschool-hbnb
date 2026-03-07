from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.user import User


class Review(BaseModel):
    """
    Review model that inherits from BaseModel
    """
    MIN_RATING = 1
    MAX_RATING = 5

    def __init__(self, text, rating, place, user):
        """
        Initialize new review instance

        Args:
            text (str): The text of the review
            rating (int): The rating of the review
            place (Place): The place being reviewed
            user (User): The user who wrote the review
        """
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self):
        """
        Get the text of the review

        Returns:
            str: The text of the review
        """
        return self.__text

    @text.setter
    def text(self, value):
        """
        Set the text of the review

        Args:
            value (str): The text to set
        """
        value = value.strip()

        if not value:
            raise ValueError("Text cannot be empty")

        if not isinstance(value, str):
            raise TypeError("Text must be a string")


        self.__text = value

    @property
    def rating(self):
        """
        Get the rating of the review

        Returns:
            int: The rating of the review
        """
        return self.__rating

    @rating.setter
    def rating(self, value):
        """
        Set the rating of the review

        Args:
            value (int): The rating to set

        Raises:
            TypeError: If the rating is not an integer
            ValueError: If the rating is not between MIN_RATING and MAX_RATING
        """
        if not isinstance(value, int):
            raise TypeError("Rating must be an integer")

        if value < self.MIN_RATING or value > self.MAX_RATING:
            raise ValueError(f"Rating must be between {self.MIN_RATING} and {self.MAX_RATING}")

        self.__rating = value

    @property
    def place(self):
        """
        Get the Place instance
        """
        return self.__place

    @place.setter
    def place(self, value):
        """
        Set and validate the Place instance

        Args:
            value (Place): The Place instance to set
        
        Raises:
            ValueError: If the value is not a Place instance
        """
        if not isinstance(value, Place):
            raise ValueError("place must be a valid instance of Place")
        self.__place = value

    @property
    def user(self):
        """
        Get the User instance
        """
        return self.__user

    @user.setter
    def user(self, value):
        """
        Set and validate the User instance
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
            'user_id': self.user.id,
            'place_id': self.place.id
        })
        return review_dict

    def to_dict_public(self):
        """
        For POST response

        Returns:
            dict: Representation of the review with
            id, text, rating, user_id, and place_id
        """
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'user_id': self.user.id,
            'place_id': self.place.id
        }

    def to_dict_list(self):
        """
        For GET/api/v1/reviews/ response

        Returns:
            dict: Representation of the review with only id, text, and rating
        """
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating
        }
