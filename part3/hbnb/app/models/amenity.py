from app import db
from app.models.base_model import BaseModel
from sqlalchemy.orm import validates

class Amenity(BaseModel):
    __tablename__ = 'amenities'
    name = db.Column(db.String(50), nullable=False)

    NAME_LENGTH_MAX = 50
    def __init__(self, name: str):
        """
        Initialize an Amenity instance.

        Args:
            name (str): The name of the amenity 
        """
        super().__init__()
        self.name = name

    @validates("name")
    def validate_name(self, key, value):
        """
        Validates the name of the amenity.
        """
        if not isinstance(value, str):
            raise TypeError(f"The {key} of the amenity must be a string")

        if not value.strip():
            raise ValueError(f"The {key} of the amenity cannot be empty")

        if len(value) > self.NAME_LENGTH_MAX:
            raise ValueError(f"The {key} of the amenity must not exceed {self.NAME_LENGTH_MAX} characters.")

        return value.strip()

    def to_dict(self):
        """
        Convert the Amenity instance to a dictionary.
        """
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }