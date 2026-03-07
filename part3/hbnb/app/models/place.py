from app.models.base_model import BaseModel
from app.models.user import User


class Place(BaseModel):
    """
    Place model that inherits from BaseModel
    """
    TITLE_MAX_LENGTH = 100
    MIN_LATITUDE = -90.0
    MAX_LATITUDE = 90.0
    MIN_LONGITUDE = -180.0
    MAX_LONGITUDE = 180.0

    def __init__(self, title, description, price, latitude, longitude, owner):
        """
        Initialize new place instance

        Args:
            title (str): The title of the place
            description (str): The description of the place
            price (float): The price of the place
            latitude (float): The latitude of the place
            longitude (float): The longitude of the place
            owner (User): The owner of the place
        """
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    @property
    def title(self):
        """
        Get the title of the place

        Returns:
            str: The title of the place
        """
        return self.__title

    @title.setter
    def title(self, value):
        """
        Set the title of the place

        Args:
            value (str): The title to set
        """
        if not isinstance(value, str):
            raise TypeError("Title must be a string")

        value = value.strip()

        if not value:
            raise ValueError("Title of place cannot be empty")

        if len(value) > self.TITLE_MAX_LENGTH:
            raise ValueError("Title must not exceed 100 characters")

        self.__title = value

    @property
    def description(self):
        """
        Get the description of the place

        Returns:
            str: The description of the place
        """
        return self.__description

    @description.setter
    def description(self, value):
        """
        Set the description of the place

        Args:
            value (str): The description to set

        Raises:
            TypeError: If value is not a string
        """
        if not isinstance(value, str):
            raise TypeError("Description must be a string")

        self.__description = value

    @property
    def price(self):
        """
        Get the price of the place

        Returns:
            float: The place price
        """
        return self.__price

    @price.setter
    def price(self, value):
        """
        Set the price of the place

        Args:
            value (float): The price to set

        Raises:
            TypeError: If value is not a number
            ValueError: If value is negative or None
        """
        if value is None:
            raise ValueError("Price required")

        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")

        if value < 0:
            raise ValueError("Price should be a non-negative float")

        self.__price = float(value)

    @property
    def latitude(self):
        """
        Get the latitude coordinate of the place

        Returns:
            float: The latitude of the place
        """
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        """
        Set the latitude coordinate of the place

        Args:
            value (float): The latitude to set

        Raises:
            TypeError: If value is not a number
            ValueError: If value is outside the valid range or None
        """
        if value is None:
            raise ValueError("Latitude is required for this place")

        if isinstance(value, int):
            value = float(value)

        if not isinstance(value, float):
            raise TypeError("Latitude must be a float")

        if value < self.MIN_LATITUDE or value > self.MAX_LATITUDE:
            raise ValueError(f"Latitude must be within the range of {self.MIN_LATITUDE} to {self.MAX_LATITUDE}")

        self.__latitude = value

    @property
    def longitude(self):
        """
        Get the longitude coordinate of the place

        Returns:
            float: The longitude of the place
        """
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        """
        Set the longitude coordinate of the place
        """
        if isinstance(value, int):
            value = float(value)

        if not isinstance(value, float):
            raise TypeError("Longitude must be a float")

        if value is None:
            raise ValueError("Longitude is required for this place")

        if value < self.MIN_LONGITUDE or value > self.MAX_LONGITUDE:
            raise ValueError(f"Longitude must be within the range of {self.MIN_LONGITUDE} to {self.MAX_LONGITUDE}")

        self.__longitude = value

    @property
    def owner(self):
        """
        Get the owner of the place

        Returns:
            User: The owner of the place
        """
        return self.__owner

    @owner.setter
    def owner(self, value):
        """
        Set the owner of the place

        Args:
            value (User): The owner to set
        Raises:
            ValueError: If value is None
            TypeError: If value is not an instance of User
        """
        if value is None:
            raise ValueError("Owner required for this place")

        if not isinstance(value, User):
            raise TypeError("Owner must be an instance of User")

        self.__owner = value

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def to_dict(self):
        """
        Serialize the place object for POST response

        Returns:
            dict: Full place data including owner_id and amenity list.
        """
        place_dict = super().to_dict()
        place_dict.update({
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner.id if self.owner else None,
            'amenities': [amenity.to_dict_public() for amenity in self.amenities]
        })
        return place_dict

    def to_dict_list(self):
        """
        Serialize the place object for GET /places/ list response

        Returns:
            dict: Minimal place data with id, title, latitude, and longitude.
        """
        return {
            'id': self.id,
            'title': self.title,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    def to_dict_detail(self):
        """
        Serialize the place object for GET /places/<id> detail response

        Returns:
            dict: Detailed place data including nested owner and amenities.
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': self.owner.to_dict_public(),
            'amenities': [amenity.to_dict_public() for amenity in self.amenities]
        }
