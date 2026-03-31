from app import db
from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.user import User
from sqlalchemy.orm import validates


class Review(BaseModel):
    """
    Review model that inherits from BaseModel
    """
    MIN_RATING = 1
    MAX_RATING = 5

    __tablename__ = 'reviews'

    text = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    # Foreign Keys
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    @validates('rating')
    def validate_rating(self, key, value):
        """
        Validate the rating of the review

        Returns:
            int: The rating of the review
        """
        if value < self.MIN_RATING or value > self.MAX_RATING:
            raise ValueError(f"Rating must be between {self.MIN_RATING} and {self.MAX_RATING}")

        return value

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
