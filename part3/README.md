# Part 3: Enhanced Backend with Authentication and Database Integration



| Endpoint                     | Method | Action            | Owner | Client | Admin |
|------------------------------|--------|-------------------|-------|--------|-------|
| `/places/`                   | POST   | Create a place    | ✅     | ✅      | ✅     |
| `/places/<place_id>`         | PUT    | Update own place  | ✅     | ❌      | ✅     |
| `/places/<place_id>`         | DELETE | Delete own place  | ✅     | ❌      | ✅     |
| `/places/<place_id>`         | PUT    | Update any place  | ❌     | ❌      | ✅     |
| `/places/<place_id>/reviews` | POST   | Create a review   | ✅     | ✅      | ✅     |
| `/reviews/<review_id>`       | DELETE | Delete own review | ✅     | ❌      | ✅     |
| `/reviews/<review_id>`       | DELETE | Delete any review | ❌     | ❌      | ✅     |
| `/users/`                    | POST   | Create a user     | ❌     | ❌      | ✅     |
| `/users/<user_id>`           | PUT    | Update a user     | ❌     | ❌      | ✅     |
| `/amenities/`                | POST   | Create an amenity | ❌     | ❌      | ✅     |
| `/amenities/<amenity_id>`    | PUT    | Update an amenity | ❌     | ❌      | ✅     |


# Testing Endpoints

Test Place Creation (POST /api/v1/places/):

```bash
curl -X POST "http://127.0.0.1:5000/api/v1/places/" -d '{"title": "New Place"}' -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json"
```

Test Unauthorized Place Update (PUT /api/v1/places/<place_id>):

```bash
curl -X PUT "http://127.0.0.1:5000/api/v1/places/<place_id>" -d '{"title": "Updated Place"}' -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json"
```
Expected Response for Unauthorized Action:

```bash
{
    "error": "Unauthorized action"
}
```

Test Creating a Review (POST /api/v1/reviews/):

```bash
curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" -d '{"place_id": "<place_id>", "text": "Great place!"}' -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json"
```
Test Updating a Review (PUT /api/v1/reviews/<review_id>):

```bash
curl -X PUT "http://127.0.0.1:5000/api/v1/reviews/<review_id>" -d '{"text": "Updated review"}' -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json"
```
Test Deleting a Review (DELETE /api/v1/reviews/<review_id>):

curl -X DELETE "http://127.0.0.1:5000/api/v1/reviews/<review_id>" -H "Authorization: Bearer <your_token>"
Test Modifying User Data (PUT /api/v1/users/<user_id>):

curl -X PUT "http://127.0.0.1:5000/api/v1/users/<user_id>" -d '{"first_name": "Updated Name"}' -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json"


# Initialize the Database and Test the Integration

After models is defined and the repository is set up, you need to initialize the database to create the models table.

To initialize the database and create the table, run:

```bash
flask shell
>>> from app import db
>>> db.create_all()
```
