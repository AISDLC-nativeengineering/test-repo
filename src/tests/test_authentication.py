import unittest
from datetime import datetime, timedelta
from src.authentication import login, validate_session

class TestAuthentication(unittest.TestCase):

    def test_login_success(self):
        response, token = login("example@example.com", "securepassword123")
        self.assertEqual(response["message"], "Login successful")
        self.assertIsNotNone(token)

    def test_login_failure(self):
        response, token = login("example@example.com", "wrongpassword")
        self.assertEqual(response["message"], "Invalid credentials")
        self.assertIsNone(token)

    def test_session_validation(self):
        response, token = login("example@example.com", "securepassword123")
        self.assertTrue(validate_session(token))

    def test_session_timeout(self):
        response, token = login("example@example.com", "securepassword123")
        # Simulate expiration
        session = datetime.now() - timedelta(minutes=16)
        self.assertFalse(validate_session(token))

if __name__ == "__main__":
    unittest.main()