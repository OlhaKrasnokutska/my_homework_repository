import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_birthdays_success(self):
        response = self.client.get('/birthdays?month=january&department=HR')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('total', data)
        self.assertIn('employees', data)

    def test_get_birthdays_missing_parameters(self):
        response = self.client.get('/birthdays')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

    def test_get_anniversaries_success(self):
        response = self.client.get('/anniversaries?month=january&department=HR')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('total', data)
        self.assertIn('employees', data)

    def test_get_anniversaries_missing_parameters(self):
        response = self.client.get('/anniversaries')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
