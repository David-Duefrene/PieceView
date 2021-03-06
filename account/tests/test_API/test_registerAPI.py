from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

from account.models import CustomUser


class RegisterAPITest(APITestCase):
    """Test the Register API.

        Attributes:
        Methods:
            setUp(self): resets the self.user_data every test
            register(self): registers the user with self.user_data
    """
    def setUp(self):
        self.user_data = {
            'username': 'TestUser', 'email': 'test@test.com',
            'password': 'password', 'first_name': '', 'last_name': ''
        }

    def register(self):
        """register Registers a user via post.

            Returns: server response
        """
        return self.client.post(
            reverse('api_account'), self.user_data, format='json')

    def test_can_create_account(self):
        """Tests that we can create an account"""
        self.register()
        self.assertTrue(
            CustomUser.objects.get(username=self.user_data['username']))

    def test_can_create_account_with_first_name(self):
        """Tests that we can create an account with a first name"""
        self.user_data['first_name'] = 'Test'
        response = self.register()
        testUser = CustomUser.objects.get(username=self.user_data['username'])

        self.assertTrue(testUser)
        self.assertEqual(
            response.data['user']['first_name'], self.user_data['first_name']
        )

    def test_can_create_account_with_last_name(self):
        """Tests that we can create an account with a last name"""
        self.user_data['last_name'] = 'Test'
        response = self.register()
        testUser = CustomUser.objects.get(username=self.user_data['username'])

        self.assertTrue(testUser)
        self.assertEqual(
            response.data['user']['last_name'], self.user_data['last_name']
        )

    def test_fails_missing_username(self):
        """Tests that response data contains ErrorDetail for username if missing
        username
        """
        self.user_data['username'] = None
        response = self.register()

        self.assertEqual(
            response.data['username'],
            [ErrorDetail(string='This field may not be null.', code='null')]
        )

    def test_fails_missing_email(self):
        """Tests that response data contains ErrorDetail for email if missing
        email
        """
        self.user_data['email'] = None
        response = self.register()

        self.assertEqual(
            response.data['email'],
            [ErrorDetail(string='This field may not be null.', code='null')]
        )

    def test_fails_missing_password(self):
        """Tests that response data contains ErrorDetail for password if missing
        password
        """
        self.user_data['password'] = None
        response = self.register()
        self.assertEqual(
            response.data['password'],
            [ErrorDetail(string='This field may not be null.', code='null')]
        )
