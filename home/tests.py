from django.test import TestCase, SimpleTestCase

# Create your tests here.

# test case kiem thu phan mem
class SimpleTests(SimpleTestCase):
    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
