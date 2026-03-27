from app import db
from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity model that inherits from BaseModel
    """
    NAME_MAX_LENGTH = 50

    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False, unique=True)

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
