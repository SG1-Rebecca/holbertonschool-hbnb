from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()

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
        self.user_repo.update(user_id, user_data)

    #    ====================== AMENITY ===========================

    def create_amenity(self, amenity_data):
        existing_amenity = self.amenity_repo.get_by_attribute('name', amenity_data['name'])
        if existing_amenity:
            raise ValueError("Amenity already exists")

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
