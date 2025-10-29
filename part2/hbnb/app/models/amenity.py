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

    def _validate_name_length(self):
        if len(self.name) > self.NAME_LENGTH_MAX:
            raise ValueError(f"The name of the amenity must no exceed {self.NAME_LENGTH_MAX} characters.")
        
