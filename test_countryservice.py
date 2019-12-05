import unittest
from countryservice import app


class CounstryServiceTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        return super().tearDown()

    def test_countries(self):
        response = self.app.get('/countries', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # To test unauthorized

    def test_countries_query(self):
        response = self.app.get('/countries/NL', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type == 'application/json')


if __name__ == "__main__":
    unittest.main()
