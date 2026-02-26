from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity model that inherits from BaseModel
    """
    NAME_MAX_LENGTH = 50

    def __init__(self, name):
        """
        Initialize new amenity instance

        Args:
            name (str): The name of the amenity
        """
        super().__init__()
        self.name = name

    @property
    def name(self):
        """
        Get the name of the amenity

        Returns:
            str: The name of the amenity
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Set the name of the amenity

        Args:
            value (str): The name to set

        Raises:
            TypeError: If value is not a string
            ValueError: If value is empty or exceeds maximum length
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string")

        value = value.strip()

        if not value:
            raise ValueError("Name cannot be empty")

        if len(value) > self.NAME_MAX_LENGTH:
            raise ValueError("Name must not exceed 50 characters")

        self._name = value

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
