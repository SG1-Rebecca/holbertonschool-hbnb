from app.models.base_model import BaseModel

class Amenity(BaseModel):
    """
    """
    def __init__(self, name):
        """
        """
        super().__init__()
        self.name = name

    def validate_name(self):
        """
        """
        if not isinstance(self.name, str):
            raise TypeError("The name of the amenity must be a string")

        if len(self.name) > 50:
            raise ValueError("The name of the amenity must not exceed 50 characters.")

        if len(self.name) == 0:
            raise ValueError("The name of the amenity cannot be empty")