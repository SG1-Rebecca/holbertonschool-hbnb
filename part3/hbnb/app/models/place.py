from app import db
from app.models.base_model import BaseModel
from app.models.user import User
from sqlalchemy.orm import validates


class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)

    TITLE_MAX_LENGTH = 100
    DESC_MAX_LENGTH = 1500
    PRICE_MIN_VALUE = 0
    LATITUDE_MIN = -90.0
    LATITUDE_MAX = 90.0
    LONGITUDE_MIN = -180.0
    LONGITUDE_MAX = 180.0

    def __init__(self, title: str, description: str, price: str, latitude: float, longitude: float, owner):
        """
        Initialize a Place instance

        Args:
            title (str): The title of the place.
            description (str): A description of the place.
            price (float): The price of the place.
            latitude (float): The latitude of the place.
            longitude (float): The longitude of the place.
            owner (User): The owner of the place.
        """
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        #self.reviews = []
        #self.amenities = []

    @validates("title")
    def validate_title(self, key, value):
        """
        Validate the title of the place.
        """
        if not isinstance(value, str):
            raise TypeError(f"The {key} must be a string")

        if len(value) > self.TITLE_MAX_LENGTH:
            raise ValueError(f"The {key} of the place must have a maximum length of {self.TITLE_MAX_LENGTH} character")

        if not value.strip():
            raise ValueError(f"The {key} must be a non-empty string")

        return value.strip()

    @validates("description")
    def validate_description(self, key, value):
        """
        Validate the description of the place.
        """
        if not isinstance(value, str):
            raise TypeError(f"The {key} must be a string")

        if not value.strip():
            raise ValueError(f"The {key} must be a non-empty string")

        if len(value.strip()) > self.DESC_MAX_LENGTH:
            raise ValueError(f"The {key} must be less than {self.DESC_MAX_LENGTH} characters")

        return value.strip()

    @validates("price")
    def validate_price(self, key, value):
        """
        Validate the price of the place.
        """
        if value is None:
            raise ValueError(f"{key} is required for a place")

        if isinstance(value, int):
            value = float(value)

        if not isinstance(value, (float, int)):
            raise TypeError(f"The {key} must be a float or integer")

        if value <= self.PRICE_MIN_VALUE:
            raise ValueError(f"The {key} must be a positive value")
        return float(value)

    @validates("latitude")
    def validate_latitude(self, key, value):
        """
        Get the latitude of the place.
        """
        if isinstance(value, int):
            value = float(value)

        if value is None:
            raise ValueError(f"{key} is required for a place")

        if not isinstance(value, float):
            raise TypeError(f"{key} must be a float")

        if value < self.LATITUDE_MIN or value > self.LATITUDE_MAX:
            raise ValueError(f"{key} must be within the range of {self.LATITUDE_MIN} to {self.LATITUDE_MAX}")
        return value

    @validates("longitude")
    def validate_longitude(self, key, value):
        """
        Get the longitude of the place.
        """
        if isinstance(value, int):
            value = float(value)

        if value is None:
            raise ValueError(f"{key} is required for a place")

        if not isinstance(value, float):
            raise TypeError(f"{key} must be a float")

        if value < self.LONGITUDE_MIN or value > self.LONGITUDE_MAX:
            raise ValueError(f"{key} must be within the range of {self.LONGITUDE_MIN} to {self.LONGITUDE_MAX}")
        return value

    @property
    def owner(self):
        """
        Get the owner of the place.
        """
        return self.__owner

    @owner.setter
    def owner(self, value):
        """
        Set and validate the owner of the place
        """
        if value is None:
            raise ValueError("Owner is required for a place")

        if not isinstance(value, User):
            raise TypeError("The owner must be an instance of User")

        self.__owner = value

    def add_review(self, review):
        """
        Add a review to the place.
        """
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """
        Add an amenity to the place.
        """
        self.amenities.append(amenity)

    def to_dict(self):
        return{
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
            
        }

    def to_dict_list(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': self.owner.to_dict(),
            'amenities': [amenity.to_dict() for amenity in self.amenities],
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
