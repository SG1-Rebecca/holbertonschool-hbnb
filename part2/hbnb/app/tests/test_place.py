import unittest
from app.models.place import Place
from app.models.user import User
from app.models.review import Review

class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        owner = User(
            first_name="Alice",
            last_name="Smith",
            email="alice.smith@example.com"
        )
        place = Place(
            title="Palace",
            description="A nice place to stay",
            price=150.0,
            latitude=37.7749,
            longitude=-122.4194,
            owner=owner
        )

        review = Review(
            text="Great stay!",
            rating=5,
            place=place,
            user=owner
        )
        place.add_review(review)

        self.assertEqual(place.title, "Palace")
        self.assertEqual(place.price, 150.0)
        self.assertEqual(len(place.reviews), 1)
        self.assertEqual(place.reviews[0].text, "Great stay!")
        print("Place creation test passed!")

if __name__ == '__main__':
    unittest.main()