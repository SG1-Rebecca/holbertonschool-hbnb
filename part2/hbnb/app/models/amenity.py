from base_model import BaseModel

class Amenity(BaseModel):
    """
    """
    def __init__(self, name):
        """
        """
        super().__init__()
        self.name = name

    def check_length(self, name):
        if len(self.name) > 50:
            raise ValueError("The name of the amenity must no exceed 50 characters.")
        
    def format_name(self):
        if not isinstance(self.name, str):
            raise TypeError("The name of the amenity must be a string")
