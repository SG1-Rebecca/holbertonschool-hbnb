import unittest
from app.models.amenity import Amenity
import json
from app import create_app

class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Wi-Fi"
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('id', data)
        self.assertEqual(data['name'], 'Wi-Fi')

    def test_create_amenity_invalid_data(self):
        # use trailing slash consistently to avoid redirects
        response = self.client.post('/api/v1/amenities/', json={
            "name": " "
        })
        self.assertEqual(response.status_code, 400)

        name_too_long = "A" * 51
        response = self.client.post('/api/v1/amenities/', json={
            "name": name_too_long
        })
        self.assertEqual(response.status_code, 400)

    def test_get_all_amenities(self):
        # 1. Create  amenities
        self.client.post('/api/v1/amenities/', json={
            "name": "Parking"
        })
        self.client.post('/api/v1/amenities/', json={
            "name": "Sauna"
        })

        # 2.Retrieve the list of amenities
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_get_amenity(self):
        # 1. Create  amenities
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Gym"
        })
        data = json.loads(response.data)
        amenity_id = data['id']

        # Retrieve amenity
        response = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertEqual(data['id'], amenity_id)
        self.assertEqual(data['name'], "Gym")

    def test_get_amenity_not_found(self):
        # Try to retrieve an amenity that does not exist
        response = self.client.get('/api/v1/amenities/000000')
        self.assertEqual(response.status_code, 404)

    def test_update_amenity(self):
        # 1. Create amenity
        create_response = self.client.post('/api/v1/amenities/', json={
            "name": "Wifi"
        })
        amenity_id = json.loads(create_response.data)['id']

        # Update amenity
        response = self.client.put(f'/api/v1/amenities/{amenity_id}', json={
            "name": "Starlink"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Starlink')

if __name__ == '__main__':
    unittest.main()