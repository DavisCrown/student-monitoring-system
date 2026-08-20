from django.test import TestCase
from .models import User
# Create your tests here.

class UserModelTestCase(TestCase):
    def test_create_user_with_role(self):
        self.client_user = User.objects.create_user(username='assoumani', password='test123', role='student')
        self.assertEqual(self.client_user.role, 'student')