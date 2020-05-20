from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework.exceptions import ErrorDetail

from account.models import CustomUser


class EditProfileAPITest(APITestCase):
    """Test the Edit Profile API"""
    def setUp(self):
        self.client = APIClient()
        # Data we are going to update with
        self.updatedData = {
            'email': 'updateTest@test.com',
            'first_name': 'updateFirstTest',
            'last_name': 'updateLastTest'
        }

        # Creates a User
        self.data = {
            'username': 'TestUser',
            'email': 'test@test.com',
            'password': 'password',
            'first_name': 'first_test',
            'last_name': 'last_test'
        }

        self.client.post(reverse('register_API'), self.data, format='json')
        self.assertTrue(CustomUser.objects.get(username=self.data['username']))

    def test_can_update_user_profile(self):
        """Tests that we can update the user profile."""
        token = self.client.post(
            reverse('log_API'),
            {
                'username': self.data['username'],
                'password': self.data['password']
            },
            format='json'
        ).data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        self.client.put(
            reverse('edit_account'),
            self.updatedData,
            format='json'
        )
        user = CustomUser.objects.get(username=self.data['username'])

        self.assertEqual(user.first_name, self.updatedData['first_name'])
        self.assertEqual(user.last_name, self.updatedData['last_name'])
        self.assertEqual(user.email, self.updatedData['email'])

    def test_first_name_is_optional(self):
        """Tests that the first name field is optional."""
        self.updatedData['first_name'] = ''
        token = self.client.post(
            reverse('log_API'),
            {
                'username': self.data['username'],
                'password': self.data['password']
            },
            format='json'
        ).data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        self.client.put(
            reverse('edit_account'),
            self.updatedData,
            format='json'
        )
        user = CustomUser.objects.get(username=self.data['username'])

        self.assertEqual(user.first_name, self.updatedData['first_name'])

    def test_last_name_is_optional(self):
        """Tests that the last name field is optional."""
        self.updatedData['last_name'] = ''
        token = self.client.post(
            reverse('log_API'),
            {
                'username': self.data['username'],
                'password': self.data['password']
            },
            format='json'
        ).data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        self.client.put(
            reverse('edit_account'),
            self.updatedData,
            format='json'
        )
        user = CustomUser.objects.get(username=self.data['username'])

        self.assertEqual(user.last_name, self.updatedData['last_name'])

    def test_email_is_optional(self):
        """Tests that th email field is optional."""
        self.updatedData['email'] = ''
        token = self.client.post(
            reverse('log_API'),
            {
                'username': self.data['username'],
                'password': self.data['password']
            },
            format='json'
        ).data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        self.client.put(
            reverse('edit_account'),
            self.updatedData,
            format='json'
        )
        user = CustomUser.objects.get(username=self.data['username'])

        self.assertEqual(user.email, self.updatedData['email'])

    def test_bad_email_is_rejected(self):
        """Tests a improperly formatted email address is rejected."""
        self.updatedData['email'] = ''
        token = self.client.post(
            reverse('log_API'),
            {
                'username': self.data['username'],
                'password': self.data['password'],
                'email': 'incorrect'
            },
            format='json'
        ).data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = self.client.put(
            reverse('edit_account'),
            self.updatedData,
            format='json'
        )
        user = CustomUser.objects.get(username=self.data['username'])

        # email should be left as original email address
        self.assertEqual(user.email, self.updatedData['email'])
        # And we should get a HTTP 400 with error code.
        self.assertEqual(response.status_code, 400)
        # Eventually this needs to return a custom error instead of blank
        # For now the blank error will do
        self.assertEqual(
            response.data['email'],
            [ErrorDetail(string='This field may not be blank.', code='blank')]
        )
