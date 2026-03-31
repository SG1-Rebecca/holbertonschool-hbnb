from app.models import User, Place, Review, Amenity

from app.persistence.repository import SQLAlchemyRepository
from app.services.repositories.user_repository import UserRepository
from app.services.repositories.place_repository import PlaceRepository
from app.services.repositories.review_repository import ReviewRepository
from app.services.repositories.amenity_repository import AmenityRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()
        self.amenity_repo = AmenityRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)

        if not user:
            return None

        if 'password' in user_data:
            user.hash_password(user_data['password'])

        update_data = {}
        for field in ('first_name', 'last_name', 'email'):
            if field in user_data:
                update_data[field] = user_data[field]

        self.user_repo.update(user_id, update_data)
        return user

    #    ====================== AMENITY ===========================

    def create_amenity(self, amenity_data):
        existing_amenity = self.amenity_repo.get_amenity_by_name(amenity_data['name'])
        if existing_amenity:
            raise ValueError(f'{amenity_data["name"]} already exists!')

        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)

        if not amenity:
            return None

        if 'name' in amenity_data:
            amenity.name = amenity_data['name']

        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity

    #    ====================== PLACE ===========================

    def create_place(self, place_data):
        # Validate and create a place with owner and amenities
        # Remove owner_id from place_data and fetch the owner object
        owner_id = place_data.pop('owner_id', None)

        owner = self.user_repo.get(owner_id)
        if not owner:
            raise ValueError("Owner not found")

        # Remove amenities list from place_data
        amenity_ids = place_data.pop('amenities', [])

        # Create place object without amenities first
        place = Place(
            title=place_data['title'],
            description=place_data.get('description', ''),
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner=owner
        )

        # Fetch and add amenities to the place
        for amenity_id in amenity_ids:
            amenity = self.amenity_repo.get(amenity_id)
            if not amenity:
                raise ValueError("Amenity not found")
            place.add_amenity(amenity)

        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)

        if not place:
            return None

        # Update only permitted fields: title, description, price
        update_data = {}

        for field in ('title', 'description', 'price'):
            if field in place_data:
                update_data[field] = place_data[field]

        self.place_repo.update(place_id, update_data)
        return place

    #    ====================== REVIEW ===========================

    def create_review(self, review_data):

        user = self.user_repo.get(review_data['user_id'])
        if not user:
            raise ValueError("user not found")

        place = self.place_repo.get(review_data['place_id'])
        if not place:
            raise ValueError("place not found")

        # Check if user already reviewed this place
        if any(review.user.id == user.id for review in place.reviews):
            raise ValueError("User already reviewed this place")

        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            user=user,
            place=place
        )

        place.reviews.append(review)

        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        # Fetch reviews for a specific place
        place = self.place_repo.get(place_id)

        if not place:
            raise ValueError("Place not found")
        return place.reviews

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)

        if not review:
            raise ValueError("Review not found")

        if 'text' in review_data:
            review.text = review_data['text']
        if 'rating' in review_data:
            review.rating = review_data['rating']

        self.review_repo.update(review_id, review_data)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)

        if not review:
            raise ValueError("Review not found")

        place = review.place
        place.reviews = [review for review in place.reviews if review.id != review_id]

        self.review_repo.delete(review_id)
