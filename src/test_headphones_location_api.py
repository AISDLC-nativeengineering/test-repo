import unittest
from headphones_location_api import app

class TestHeadphonesLocationAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_location_no_headphone_id(self):
        response = self.app.get('/headphones/location')
        self.assertEqual(response.status_code, 400)
        self.assertIn('headphone_id is required', response.get_data(as_text=True))

    def test_get_location_not_found(self):
        response = self.app.get('/headphones/location', query_string={'headphone_id': 'nonexistent_id'})
        self.assertEqual(response.status_code, 404)
        self.assertIn('No location data available', response.get_data(as_text=True))

# NOTE: Mocking database connection and valid test will be implemented separately

if __name__ == '__main__':
    unittest.main()