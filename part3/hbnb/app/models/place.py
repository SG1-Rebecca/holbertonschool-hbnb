from app.models.base_model import BaseModel
from app.models.user import User


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    """
    TITLE_MAX_LENGTH = 100
    DESC_MAX_LENGTH = 1500
    PRICE_MIN_VALUE = 0
    LATITUDE_MIN = -90.0
    LATITUDE_MAX = 90.0
    LONGITUDE_MIN = -180.0
    LONGITUDE_MAX = 180.0

    def __init__(self, title, description, price, latitude, longitude, owner):
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
        self.reviews = []
        self.amenities = []

    @property
    def title(self):
        """
        Validate the title of the place.
        """
        return self.__title

    @title.setter
    def title(self, value):
        """
        Set and validate the title of the place.
        """
        if not isinstance(value, str):
            raise TypeError("The title must be a string")

        if len(value) > self.TITLE_MAX_LENGTH:
            raise ValueError(f"The title of the place must have a maximum length of {self.TITLE_MAX_LENGTH} character")

        if not value.strip():
            raise ValueError("The title must be a non-empty string")

        self.__title = value.strip()

    @property
    def description(self):
        """
        Get the description of the place.
        """
        return self.__description

    @description.setter
    def description(self, value):
        """
        Validate the description of the place.
        """
        if not isinstance(value, str):
            raise TypeError("Description must be a string")

        if not value.strip():
            raise ValueError("Description must be a non-empty string")

        if len(value.strip()) > self.DESC_MAX_LENGTH:
            raise ValueError(f"Description must be less than {self.DESC_MAX_LENGTH} characters")

        self.__description = value.strip()

    @property
    def price(self):
        """
        Validate the price of the place.
        """
        return self.__price

    @price.setter
    def price(self, value):

        if value is None:
            raise ValueError("Price is required for a place")

        if isinstance(value, int):
            value = float(value)

        if not isinstance(value, (float, int)):
            raise TypeError("The price must be a float or integer")

        if value <= self.PRICE_MIN_VALUE:
            raise ValueError("The price must be a positive value")
        self.__price = float(value)

    @property
    def latitude(self):
        """
        Get the latitude of the place.
        """
        return self.__latitude

    @latitude.setter
    def latitude(self, value):

        if isinstance(value, int):
            value = float(value)

        if value is None:
            raise ValueError("Latitude is required for a place")

        if not isinstance(value, float):
            raise TypeError("Latitude must be a float")

        if value < self.LATITUDE_MIN or value > self.LATITUDE_MAX:
            raise ValueError(f"Latitude must be within the range of {self.LATITUDE_MIN} to {self.LATITUDE_MAX}")
        self.__latitude = value

    @property
    def longitude(self):
        """
        Get the longitude of the place.
        """
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if isinstance(value, int):
            value = float(value)

        if value is None:
            raise ValueError("Longitude is required for a place")

        if not isinstance(value, float):
            raise TypeError("Longitude must be a float")

        if value < self.LONGITUDE_MIN or value > self.LONGITUDE_MAX:
            raise ValueError(f"Longitude must be within the range of {self.LONGITUDE_MIN} to {self.LONGITUDE_MAX}")
        self.__longitude = value

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
        place_dict = super().to_dict()
        place_dict.update({
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner.id
        })
        return place_dict

    def to_dict_list(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': self.owner.to_dict(),
            'amenities': self.amenities,
            'reviews': self.reviews
        }
