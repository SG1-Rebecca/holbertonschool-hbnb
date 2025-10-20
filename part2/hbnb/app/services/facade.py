from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
# Users
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
        user = self.user_repo.get(user_id)
        if user:
            if 'email' in user_data and user_data['email'] != user.email:
                user_exist = self.get_user_by_email(user_data['email'])
                if user_exist:
                    raise ValueError("Email already registered")
            user.update(user_data)
        return user
# Places

    def create_place(self, place_data):
        # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if place:
            #update price
            if 'price' in place_data and place_data['price'] != place.price:
                place.price = place_data['price']
            #update latitude
            if 'latitude' in place_data and place_data['latitude'] != place.latitude:
                place.latitude = place_data['latitude']
            #update longitude
            if 'longitude' in place_data and place_data['longitude'] != place.longitude:
                place.longitude = place_data['longitude']
            place.update(place_data)
        return place

facade = HBnBFacade()
