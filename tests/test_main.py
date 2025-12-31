# Import required libraries
import unittest
from src.main import app

# Define a test class
class TestMain(unittest.TestCase):
    def test_home(self):
        # Create a test client
        client = app.test_client()
        
        # Make a request to the home page
        response = client.get('/')
        
        # Check the status code
        self.assertEqual(response.status_code, 200)
