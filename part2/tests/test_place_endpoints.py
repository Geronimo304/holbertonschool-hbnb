import unittest
from app import create_app

class TestPlaceEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        # Crear usuario que será dueño del place
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Lena",
            "last_name": "Jackson",
            "email": "lena@example.com"
        })
        self.assertEqual(response.status_code, 201, msg=response.get_data(as_text=True))
        user_data = response.get_json()
        self.assertIn('id', user_data)
        self.owner_id = user_data['id']


    def test_create_place_valid(self):
        response = self.client.post('/api/v1/places/', json={
            "title": "Casa en la playa",
            "description": "Hermosa casa frente al mar",
            "price": 150.0,
            "latitude": -34.9,
            "longitude": -56.2,
            "owner_id": self.owner_id,
            "amenities": [],
            "reviews": []
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('place_id', data)

    def test_create_place_invalid(self):
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "price": -10,
            "latitude": 100,
            "longitude": -200,
            "owner_id": "nonexistent",
            "amenities": [],
            "reviews": []
        })
        self.assertIn(response.status_code, (400, 404))

if __name__ == '__main__':
    unittest.main()
