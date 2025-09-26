import unittest
from src.api.app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_query_endpoint(self):
        response = self.app.post('/query', json={'question': 'What is the capital of France?'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Paris', response.data)

    def test_invalid_query(self):
        response = self.app.post('/query', json={'question': ''})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid query', response.data)

if __name__ == '__main__':
    unittest.main()