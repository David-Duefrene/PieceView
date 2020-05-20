from django.urls import reverse

from rest_framework.test import APITestCase

from account.models import CustomUser


class LoginAPITest(APITestCase):
    """Tests the Login API"""
    def setUp(self):
        self.data = {
            'username': 'TestUser',
            'email': 'test@test.com',
            'password': 'password',
            'first_name': 'first_test',
            'last_name': 'last_test'
        }

        # Create a user
        userObject = CustomUser.objects
        self.client.post(reverse('register_API'), self.data, format='json')
        self.assertTrue(userObject.get(username=self.data['username']))

    def test_valid_credentials_can_login(self):
        """
        Tests to make sure good username and passord returns a HTTP 200 code,
        a user object, and a token
        """
        login = {
            'username': self.data['username'],
            'password': self.data['password']
        }
        response = self.client.post(reverse('log_API'), login)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['user'])
        self.assertTrue(response.data['token'])
