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
    LONGITUDE_MAX = 180
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
        self.validate()

    def validate(self):
        """
        Validate the attributes of the Place instance.
        """
        self.validate_title()
        self.validate_description()
        self.validate_price()
        self.validate_coordinates()
        self.validate_owner()

    def validate_title(self):
        """
        Validate the title of the place.
        """
        if not isinstance(self.title, str):
            raise TypeError("The title must be a string")

        if len(self.title) > self.TITLE_MAX_LENGTH:
            raise ValueError(f"The title of the place must have a maximum length of {self.TITLE_MAX_LENGTH} character")

        if not self.title.strip():
            raise ValueError("The title must be a non-empty string")

    def validate_description(self):
        """
        Validate the description of the place.
        """
        if self.description is not None and not isinstance(self.description, str):
            raise TypeError("Description must be a string or None")

        if isinstance(self.description, str) and len(self.description) > self.DESC_MAX_LENGTH:
            raise ValueError(f"Description must be less than {self.DESC_MAX_LENGTH} characters")

    def validate_price(self):
        """
        Validate the price of the place.
        """
        if self.price is None:
            raise ValueError("Price is required for a place")

        if not isinstance(self.price, float):
            raise TypeError("The price must be a float")

        if self.price <= self.PRICE_MIN_VALUE:
            raise ValueError("The price must be a positive value")


    def validate_coordinates(self):
        """
        Validate the latitude and longitude of the place.
        """
        # Validate latitude
        if isinstance(self.latitude, int):
            self.latitude = float(self.latitude)

        if self.latitude is None:
            raise ValueError("Latitude is required for a place")

        if not isinstance(self.latitude, float):
            raise TypeError("Latitude must be a float")

        if self.latitude < self.LATITUDE_MIN or self.latitude > self.LATITUDE_MAX:
            raise ValueError(f"Latitude must be within the range of {self.LATITUDE_MIN} to {self.LATITUDE_MAX}")

        # Validate longitude
        if isinstance(self.longitude, int):
            self.longitude = float(self.longitude)

        if self.longitude is None:
            raise ValueError("Longitude is required for a place")

        if not isinstance(self.longitude, float):
            raise TypeError("Longitude must be a float")

        if self.longitude < self.LONGITUDE_MIN or self.longitude > self.LONGITUDE_MAX:
            raise ValueError(f"Longitude must be within the range of {self.LONGITUDE_MIN} to {self.LONGITUDE_MAX}")

    def validate_owner(self):
        """
        Validate that the owner is a User instance and exists.
        """
        if self.owner is None:
            raise ValueError("Owner is required for a place")

        if not isinstance(self.owner, User):
            raise TypeError("The owner must be an instance of User")

    def is_owner(self, user):
        """
        Check if the user is the owner of the place.

        Return:
            string: The ID of the owner if the user is the owner.
        """
        if not isinstance(user, User):
            raise TypeError("The user must be an instance of User")
        return self.owner.id == user.id