from app.models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    """
    NAME_LENGTH_MAX = 50
    def __init__(self, name):
        """
        Initialize an Amenity instance.

        Args:
            name (str): The name of the amenity 
        """
        super().__init__()
        self.name = name

    @property
    def name(self):
        """
        Get the name of the amenity.
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Set and validate the name of the amenity.
        """
        if not isinstance(value, str):
            raise TypeError("The name of the amenity must be a string")

        if not value.strip():
            raise ValueError("The name of the amenity cannot be empty")

        if len(value) > self.NAME_LENGTH_MAX:
            raise ValueError(f"The name of the amenity must not exceed {self.NAME_LENGTH_MAX} characters.")

        self.__name = value

    def to_dict(self):
        """
        Convert the Amenity instance to a dictionary."""
        amenity_dict = super().to_dict()
        amenity_dict.update({
            'name': self.name
            })
        return amenity_dict
