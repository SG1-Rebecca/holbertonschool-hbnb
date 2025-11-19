import unittest
from app.models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        amenity = Amenity(name="Wi-Fi")
        self.assertEqual(amenity.name, "Wi-Fi")
        print("Amenity creation test passed!")

    def test_amenity_invalid_type(self):
        with self.assertRaises(TypeError):
            Amenity(name=12345)
        print("Type check test passed!")

    def test_amenity_empty_string(self):
        with self.assertRaises(ValueError):
            Amenity(name="")
        print("Empty string validation passed!")

    def test_amenity_length(self):
        with self.assertRaises(ValueError):
            Amenity(name="a" * 51)
        print("Amenity length validation passed!")

if __name__ == "__main__":
    unittest.main()