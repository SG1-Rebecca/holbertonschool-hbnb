from base_model import BaseModel

class Amenity(BaseModel):
    """
    """
    NAME_LENGTH_MAX = 50
    def __init__(self, name):
        """
        """
        super().__init__()
        self.name = name

    def _validate_name(self):
        if not isinstance(self.name, str):
            raise TypeError("The name of the amenity must be a string")

        if not self.name.strip():
            raise ValueError("The name of the amenity cannot be empty")

    def check_length(self, name):
        if len(self.name) > 50:
            raise ValueError("The name of the amenity must no exceed 50 characters.")
        
