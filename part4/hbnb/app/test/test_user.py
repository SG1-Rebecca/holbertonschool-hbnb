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

if __name__ == "__main__":
    unittest.main()