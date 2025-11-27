from app import db
from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.user import User
from sqlalchemy.orm import validates


class Review(BaseModel):
    __tablename__ = 'reviews'
    id = db.Column(db.String, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.String, db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)

    MIN_RATING = 1
    MAX_RATING = 5

    def __init__(self, text: str, rating: int, place: str, user):
        """
        Initialize a Review instance.

        Args:
            text (str): The content of the review
            rating (int): The rating given to the place
            place (Place): The Place being reviewed
            user (User): The User who wrote the review
        """
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @validates("text")
    def validate_text(self, key, value):
        """
        Validate the review text
        """
        if not isinstance(value, str):
            raise ValueError(f"{key} must be a string")

        if not value.strip():
            raise ValueError(f"{key} cannot be empty")
        return value.strip()

    @validates("rating")
    def validate_rating(self, key, value):
        """
        Validate the review rating
        """
        if not isinstance(value, int) or value < self.MIN_RATING or value > self.MAX_RATING:
            raise ValueError(f"{key} must be an integer between {self.MIN_RATING} and {self.MAX_RATING}")
        return value

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
        return{
            'text': self.text,
            'rating': self.rating,
            'place_id': self.place.id,
            'user_id': self.user.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
