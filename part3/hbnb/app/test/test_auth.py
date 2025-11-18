import unittest
from app import create_app
from app.services import facade
import json

class TestAuth(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        # Créer un utilisateur de test
        self.test_user_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User'
        }
        self.test_user = facade.create_user(self.test_user_data)
    
    def test_successful_login(self):
        """Test login with valid credentials"""
        response = self.client.post('/api/v1/auth/login', 
                                   data=json.dumps({
                                       'email': 'test@example.com',
                                       'password': 'testpassword'
                                   }),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)
    
    def test_invalid_credentials(self):
        """Test login with invalid credentials"""
        response = self.client.post('/api/v1/auth/login',
                                   data=json.dumps({
                                       'email': 'test@example.com',
                                       'password': 'wrongpassword'
                                   }),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 401)
        self.assertIn('error', response.json)
    
    def test_user_not_found(self):
        """Test login with non-existent user"""
        response = self.client.post('/api/v1/auth/login',
                                   data=json.dumps({
                                       'email': 'nonexistent@example.com',
                                       'password': 'password'
                                   }),
                                   content_type='application/json')
        
        self.assertEqual(response.status_code, 401)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()