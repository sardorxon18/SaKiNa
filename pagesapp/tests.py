from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/simple/')
        self.assertEqual(response.status_code,200)
    def test_about_page_status_code(self):
        response = self.client.get('/salom/')
        self.assertEqual(response.status_code,200)
    def test_about_page_status_code(self):
        response = self.client.get('/htmlandcss/')
        self.assertEqual(response.status_code,200)
    def test_about_page_status_code(self):
        response = self.client.get('/basic/')
        self.assertEqual(response.status_code,200)