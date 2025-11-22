import unittest
from app.models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_amenity_creation(self):
        amenity = Amenity(name="Wi-Fi")
        self.assertEqual(amenity.name, "Wi-Fi")
        print("Amenity creation test passed!")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            Amenity(name="    ") 

    def test_name_type(self):
        with self.assertRaises(TypeError):
            Amenity(name=123)

    def test_name_length(self):
        with self.assertRaises(ValueError):
            Amenity(name="A" * 51)

    def test_name_valid(self):
        amenity = Amenity(name="Gym")
        self.assertEqual(amenity.name, "Gym")

if __name__ == '__main__':
    unittest.main()
