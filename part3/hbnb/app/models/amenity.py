from app import db
from app.models.base_model import BaseModel
from sqlalchemy.orm import validates

class Amenity(BaseModel):
    """
    Amenity model that inherits from BaseModel
    """

    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False, unique=True)

    @validates('name')
    def validate_name(self, key, name):
        """
        Validate the amenity name
        """
        if not isinstance(name, str):
            raise ValueError('Amenity name must be a string')

        name = name.strip()

        if not name:
            raise ValueError('Amenity name cannot be empty')

        if len(name) > 50:
            raise ValueError('Amenity name must not exceed 50 characters')

        return name.lower()

    def to_dict(self):
        """
        Convert amenity instance into a dictionary

        Returns:
            dict: Dictionary representation of amenity
        """
        amenity_dict = super().to_dict()
        amenity_dict.update({
            'name': self.name,
        })
        return amenity_dict

    def to_dict_public(self):
        """
        Return a public dictionary representation of the amenity,
        excluding timestamps
        """
        return {
            'id': self.id,
            'name': self.name
        }
