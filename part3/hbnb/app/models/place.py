from app import db
from app.models.base_model import BaseModel
from app.models.user import User
from sqlalchemy.orm import validates, relationship

# Association table to manage the many-to-many relationship between Place and Amenity.
place_amenities = (db.Table(
                            'place_amenities',
                            db.Column('place_id', db.String, db.ForeignKey('places.id'), primary_key=True),
                            db.Column('amenity_id', db.String, db.ForeignKey('amenities.id'), primary_key=True)
                            ))

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
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    # Foreign Keys
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    # Relationships
    amenities = relationship('Amenity', secondary=place_amenities, backref='places', lazy='subquery')
    reviews = relationship('Review', backref='place', lazy=True)



    @validates('price')
    def validate_price(self, key, value):
        """
        Validate the price of the place
        """
        if value < 0:
            raise ValueError("Price should be a non-negative float")
        return value

    @validates('latitude')
    def validate_latitude(self, key, value):
        """
        Validate the latitude of the place
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
        """
        if isinstance(value, int):
            value = float(value)

        if value < self.MIN_LONGITUDE or value > self.MAX_LONGITUDE:
            raise ValueError(f"Longitude must be within the range of {self.MIN_LONGITUDE} to {self.MAX_LONGITUDE}")

        return value

    def add_amenity(self, amenity):
        """
        Add an amenity to the place
        """
        if amenity not in self.amenities:
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
            'price': self.price
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
            'amenities': [amenity.to_dict_public() for amenity in self.amenities]
        }
