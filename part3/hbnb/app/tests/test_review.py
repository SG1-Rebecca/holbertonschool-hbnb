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

    def test_review_creation_valid_data(self):
        # simply ensure that creating with valid data doesn't raise
        owner = User(
            first_name="Foo",
            last_name="Bar",
            email="foo.bar@example.com"
        )
        place = Place(
            title="Test",
            description="desc",
            price=10.0,
            latitude=0.0,
            longitude=0.0,
            owner=owner
        )
        review = Review(
            text="Nice",
            rating=4,
            place=place,
            user=owner
        )
        self.assertEqual(review.text, "Nice")
        self.assertEqual(review.rating, 4)

    def test_review_get_all(self):
        owner = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        place = Place(title="Lorem", description="Ipsum", price=1.0, latitude=0, longitude=0, owner=owner)
        r1 = Review(text="one", rating=1, place=place, user=owner)
        r2 = Review(text="two", rating=2, place=place, user=owner)
        place.add_review(r1)
        place.add_review(r2)
        self.assertEqual(len(place.reviews), 2)


if __name__ == '__main__':
    unittest.main()