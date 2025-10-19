import unittest
from app.models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        amenity = Amenity(name="Wi-Fi")
        self.assertEqual(amenity.name, "Wi-Fi")
        print("Amenity creation test passed!")

if __name__ == "__main__":
    unittest.main()
