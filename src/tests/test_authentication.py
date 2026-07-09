# test_authentication.py
# Unit tests for authentication functionality.

import unittest
import json
from authentication import app

class TestAuthentication(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_login_success(self):
        data = {"username": "technician1", "password": "plaintext_password_technician1"}
        response = self.client.post('/api/v1/auth/login', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("role", response.json)
        self.assertEqual(response.json["role"], "technician")

    def test_login_failure(self):
        data = {"username": "wrong_user", "password": "wrong_password"}
        response = self.client.post('/api/v1/auth/login', json=data)
        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.json)

    def test_role_data_success(self):
        headers = {"Authorization": "Bearer mock_token"}
        response = self.client.get('/api/v1/role-data', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("role", response.json)
        self.assertEqual(response.json["role"], "technician")

    def test_role_data_failure(self):
        headers = {}
        response = self.client.get('/api/v1/role-data', headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.json)

if __name__ == "__main__":
    unittest.main()