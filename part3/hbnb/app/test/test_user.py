import unittest
from app.models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com"
        )
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertFalse(user.is_admin)  # Default value
        print("User creation test passed!")

    def test_empty_first_name(self):
        with self.assertRaises(ValueError):
            User (
                first_name="    ",
                last_name="Doe",
                email="john.doe@example.com"
            )

    def test_empty_last_name(self):
        with self.assertRaises(ValueError):
            User (
                first_name="John",
                last_name="     ",
                email="john.doe@example.com"
            )

    def test_empty_email(self):
        with self.assertRaises(ValueError):
            User (
                first_name="John",
                last_name="Doe",
                email=""
            )

    def test_format_email(self):
        with self.assertRaises(ValueError):
            User (
                first_name="John",
                last_name="Doe",
                email="johndoeexamplecom"
            )

    def test_invalid_email_type(self):
        with self.assertRaises(TypeError):
            User(
                first_name="John",
                last_name="Doe",
                email=12345  
            )

    def test_first_name_type(self):
        with self.assertRaises(TypeError):
            User(
                first_name=123,  
                last_name="Doe",
                email="john.doe@example.com"
            )

    def test_last_name_type(self):
        with self.assertRaises(TypeError):
            User(
                first_name="John",
                last_name=123,  
                email="john.doe@example.com"
            )

    def test_is_admin_default(self):
        user = User(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com"
        )
        self.assertFalse(user.is_admin)

    def test_is_admin_true(self):
        user = User(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            is_admin=True
        )
        self.assertTrue(user.is_admin)

if __name__ == '__main__':
    unittest.main()