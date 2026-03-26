from app import db
from app.models.base_model import BaseModel
from app.models.user import User
from sqlalchemy.orm import validates


class Place(BaseModel):
    """
    Place model that inherits from BaseModel
    """
    MIN_LATITUDE = -90.0
    MAX_LATITUDE = 90.0
    MIN_LONGITUDE = -180.0
    MAX_LONGITUDE = 180.0

    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)



    @validates('price')
    def validate_price(self, key, value):
        """
        Validate the price of the place

        Returns:
            float: The place price
        """
        if value < 0:
            raise ValueError("Price should be a non-negative float")
        return value

    @validates('latitude')
    def validate_latitude(self, key, value):
        """
        Validate the latitude of the place

        Returns:
            float: The latitude of the place
        """
        if isinstance(value, int):
            value = float(value)

        if value < self.MIN_LATITUDE or value > self.MAX_LATITUDE:
            raise ValueError(f"Latitude must be within the range of {self.MIN_LATITUDE} to {self.MAX_LATITUDE}")
        return value

    @validates('longitude')
    def validate_longitude(self, key, value):
        """
        Validate the longitude of the place

        Returns:
            float: The longitude of the place
        """
        if isinstance(value, int):
            value = float(value)

        if value < self.MIN_LONGITUDE or value > self.MAX_LONGITUDE:
            raise ValueError(f"Longitude must be within the range of {self.MIN_LONGITUDE} to {self.MAX_LONGITUDE}")

        return value

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
