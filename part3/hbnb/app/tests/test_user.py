import unittest
import json
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    # ============ POST =================
    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)

    # ============ GET ID =================

    def test_get_user(self):
        # 1. Create user
        create_response = self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        })
        user_id = json.loads(create_response.data)['id']
        
        # 2. Get user
        response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['email'], 'john.doe@example.com')

    def test_get_user_not_found(self):
        response = self.client.get('/api/v1/users/nonexistent-id-000')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_get_user_returns_expected_fields(self):
        create_response = self.client.post('/api/v1/users/', json={
            "first_name": "Eve",
            "last_name": "Black",
            "email": "eve.black@example.com"
        })
        user_id = json.loads(create_response.data)['id']

        response = self.client.get(f'/api/v1/users/{user_id}')
        data = json.loads(response.data)
        for field in ('id', 'first_name', 'last_name', 'email'):
            self.assertIn(field, data)

    # ============ PUT =================

      def test_update_user(self):
        create_response = self.client.post('/api/v1/users/', json={
            "first_name": "Frank",
            "last_name": "Green",
            "email": "frank.green@example.com"
        })
        user_id = json.loads(create_response.data)['id']

        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "Franklin",
            "last_name": "Green",
            "email": "frank.green@example.com"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['first_name'], 'Franklin')

    def test_update_user_not_found(self):
        response = self.client.put('/api/v1/users/nonexistent-id-000', json={
            "first_name": "Ghost",
            "last_name": "User",
            "email": "ghost@example.com"
        })
        self.assertEqual(response.status_code, 404)

    def test_update_user_invalid_data(self):
        create_response = self.client.post('/api/v1/users/', json={
            "first_name": "Grace",
            "last_name": "Hall",
            "email": "grace.hall@example.com"
        })
        user_id = json.loads(create_response.data)['id']

        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "",
            "last_name": "",
            "email": "not-an-email"
        })
        self.assertEqual(response.status_code, 400)

    def test_update_user_persists_changes(self):
        """PUT then GET should reflect the updated values."""
        create_response = self.client.post('/api/v1/users/', json={
            "first_name": "Hank",
            "last_name": "Hill",
            "email": "hank.hill@example.com"
        })
        user_id = json.loads(create_response.data)['id']

        self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "Henry",
            "last_name": "Hill",
            "email": "hank.hill@example.com"
        })

        response = self.client.get(f'/api/v1/users/{user_id}')
        data = json.loads(response.data)
        self.assertEqual(data['first_name'], 'Henry')


if __name__ == '__main__':
    unittest.main()