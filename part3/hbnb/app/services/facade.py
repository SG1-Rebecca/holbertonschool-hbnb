from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review



class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user =  self.user_repo.get(user_id)
        if not user:
            return None
    
        if 'email' in user_data and user_data['email'] != user.email:
            existing_user = self.get_user_by_email(user_data['email'])
            if existing_user:
                raise ValueError("Email already registered")
    
        user.update(user_data)
        return user

# === Amenity ===

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        self.amenity_repo.update(amenity_id, amenity_data)

# === Place ===
    def create_place(self, place_data):
        data = place_data.copy()
    
        owner_id = data.pop('owner_id')
        owner = self.get_user(owner_id)

        if not owner:
            raise ValueError(f"User with id {owner_id} not found")

        amenity_ids = data.pop('amenities', [])

        data['owner'] = owner
        place = Place(**data)

        for amenity_id in amenity_ids:
            amenity = self.get_amenity(amenity_id)
            if amenity:
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
        
        self.place_repo.update(place_id, place_data)
        return place

# === Review ===

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        if not place_id:
            raise ValueError("place_id is required")
        reviews = []
        for review in self.review_repo.get_all():
            if review.place_id == place_id:
                reviews.append(review)
        return reviews

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        if not review_id:
            raise ValueError("review_id is required")
    
    def get_review_user_place(self, user_id, place_id):
        list_reviews = self.review_repo.get_all()
        for review in list_reviews:
            if review.user_id == user_id and review.place_id == place_id:
                return review
            return None
