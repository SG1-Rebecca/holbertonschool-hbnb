import unittest
from app.models.review import Review
from app.models.place import Place
from app.models.user import User

class TestReview(unittest.TestCase):
    
    def test_review_creation(self):
        owner = User(
            first_name="Alice",
            last_name="Smith", 
            email="alice.smith@example.com"
        )
        
        place = Place(
            title="Cozy Apartment",
            description="A lovely place to stay",
            price=150.0,
            latitude=37.7749,
            longitude=-122.4194,
            owner=owner
        )
        review = Review(
            text= "Great stay!",
            rating= 5,
            place=place,
            user=owner,                
        )

        self.assertEqual(review.text, "Great stay!")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.place, place)
        self.assertEqual(review.user, owner)
        print("Review creation test passed!")


if __name__ == '__main__':
    unittest.main()
