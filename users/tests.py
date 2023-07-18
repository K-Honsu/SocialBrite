from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import UserAccount


class UserAccountTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # URL for the user creation endpoint
        self.create_user_url = ('/auth/users/')

        # Test data for user creation
        self.user_data = {
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'password': 'testpassword123',
        }

    def test_create_user(self):
        response = self.client.post(self.create_user_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the user exists in the database
        user = UserAccount.objects.get(email=self.user_data['email'])
        self.assertEqual(user.first_name, self.user_data['first_name'])
        self.assertEqual(user.last_name, self.user_data['last_name'])
        self.assertEqual(user.username, self.user_data['username'])

    def test_create_user_with_invalid_data(self):
        # Try creating a user with missing required fields
        invalid_data = {
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
        }

        response = self.client.post(self.create_user_url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
