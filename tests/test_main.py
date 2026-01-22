import unittest
import sys
import os

# Add the parent directory to the path to import from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from app import app


class TestMainApp(unittest.TestCase):
    
    def setUp(self):
        """Set up test client before each test"""
        self.app = app
        self.client = self.app.test_client()
        self.app.testing = True
    
    def test_hello_route_status_code(self):
        """Test that the root route returns 200 status code"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_hello_route_content(self):
        """Test that the root route returns the correct message"""
        response = self.client.get('/')
        self.assertIn(b'Congratulations!', response.data)
        self.assertIn(b'Your application is running in Azure Cloud', response.data)
    
    def test_hello_route_html(self):
        """Test that the response is HTML"""
        response = self.client.get('/')
        self.assertIn(b'<h1>', response.data)
        self.assertIn(b'</h1>', response.data)


if __name__ == '__main__':
    unittest.main()
