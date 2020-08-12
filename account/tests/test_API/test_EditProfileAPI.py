"""Test to make sure a user can edit their profile"""
from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework.exceptions import ErrorDetail

from account.models import CustomUser
from common.create_user import create_user


class EditProfileAPITest(APITestCase):
    """Test the Edit Profile API.

    Attributes:
        updated_data: Data we are going to update the profile with

    Methods:
        setup(self): resets the class attribute back to defaults
        update_user(self, data): updates the user with the given data
    """

    def setUp(self):
        """Set up the client, update_data, user, and response"""
        self.client = APIClient()
        # Data we are going to update with
        self.updated_data = {
            'email': 'updateTest@test.com',
            'first_name': 'updateFirstTest',
            'last_name': 'updateLastTest'
        }
        self.user = create_user()
        self.response = None

    def update_user(self):
        """Update the user's profile

        Updates the user's profile with updated_data and updates the user and
        adds the server response response.
        """
        self.client.force_authenticate(user=self.user)
        self.response = self.client.patch(
            reverse('edit_account'), self.updated_data, format='json'
        )
        self.user = CustomUser.objects.get(username=self.user.username)

    def test_can_update_user_profile(self):
        """Test that we can update the user profile."""
        self.update_user()
        self.assertEqual(self.user.first_name, self.updated_data['first_name'])
        self.assertEqual(self.user.last_name, self.updated_data['last_name'])
        self.assertEqual(self.user.email, self.updated_data['email'])

    def test_first_name_is_optional(self):
        """Test that the first name field is optional."""
        self.updated_data['first_name'] = ''
        self.update_user()
        self.assertEqual(self.user.first_name, self.updated_data['first_name'])

    def test_last_name_is_optional(self):
        """Test that the last name field is optional."""
        self.updated_data['last_name'] = ''
        self.update_user()
        self.assertEqual(self.user.last_name, self.updated_data['last_name'])

    def test_email_is_optional(self):
        """Test that th email field is optional."""
        self.updated_data['email'] = ''
        self.update_user()
        self.assertEqual(self.user.email, self.updated_data['email'])

    def test_bad_email_is_rejected(self):
        """Test a improperly formatted email address is rejected."""
        self.updated_data['email'] = ''
        self.update_user()

        # email should be left as original email address
        self.assertEqual(self.user.email, self.updated_data['email'])
        # And we should get a HTTP 400 with error code.
        self.assertEqual(self.response.status_code, 400)
        # Eventually this needs to return a custom error instead of blank
        # For now the blank error will do
        self.assertEqual(
            self.response.data['email'],
            [ErrorDetail(string='This field may not be blank.', code='blank')]
        )
