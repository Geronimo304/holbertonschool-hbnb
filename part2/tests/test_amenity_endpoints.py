import unittest
from app import create_app
import uuid

class TestAmenityEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity_valid(self):
        response = self.client.post('/api/v1/amenity/', json={
            "name": "WiFi"
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'WiFi')

    def test_create_amenity_duplicate(self):
        self.client.post('/api/v1/amenity/', json={"name": "Piscina"})
        response = self.client.post('/api/v1/amenity/', json={"name": "Piscina"})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
