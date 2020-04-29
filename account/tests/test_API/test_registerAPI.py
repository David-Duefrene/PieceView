from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

from account.models import CustomUser


class RegisterAPITest(APITestCase):
    """Test the Register API"""
    def setUp(self):
        self.data = {
            'username': 'TestUser',
            'email': 'test@test.com',
            'password': 'password',
            'first_name': '',
            'last_name': ''
        }

    def test_can_create_account(self):
        """Tests that we can create an account"""
        self.client.post(reverse('register_API'), self.data, format='json')
        self.assertTrue(CustomUser.objects.get(username=self.data['username']))

    def test_can_create_account_with_first_name(self):
        """Tests that we can create an account with a first name"""
        self.data['first_name'] = 'Test'
        response = self.client.post(
            reverse('register_API'),
            self.data, format='json'
        )
        testUser = CustomUser.objects.get(username=self.data['username'])
        self.assertTrue(testUser)
        self.assertEqual(
            response.data['user']['first_name'],
            self.data['first_name']
        )

    def test_can_create_account_with_last_name(self):
        """Tests that we can create an account with a last name"""
        self.data['last_name'] = 'Test'
        response = self.client.post(
            reverse('register_API'),
            self.data, format='json'
        )
        testUser = CustomUser.objects.get(username=self.data['username'])
        self.assertTrue(testUser)
        self.assertEqual(
            response.data['user']['last_name'],
            self.data['last_name']
        )

    def test_fails_missing_username(self):
        """
        Tests that response data contains ErrorDetail for username if missing
        username
        """
        self.data['username'] = None
        response = self.client.post(
            reverse('register_API'),
            self.data, format='json'
        )

        self.assertEqual(
            response.data['username'],
            [ErrorDetail(string='This field may not be null.', code='null')]
        )

    def test_fails_missing_email(self):
        """
        Tests that response data contains ErrorDetail for email if missing
        email
        """
        self.data['email'] = None
        response = self.client.post(
            reverse('register_API'),
            self.data, format='json'
        )

        self.assertEqual(
            response.data['email'],
            [ErrorDetail(string='This field may not be null.', code='null')]
        )

    def test_fails_missing_password(self):
        """
        Tests that response data contains ErrorDetail for password if missing
        password
        """
        self.data['password'] = None
        response = self.client.post(
            reverse('register_API'),
            self.data, format='json'
        )

        self.assertEqual(
            response.data['password'],
            [ErrorDetail(string='This field may not be null.', code='null')]
        )
