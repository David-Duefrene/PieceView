from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

from account.models import CustomUser


class ContactsAPITest(APITestCase):
    """Test the Contacts API.
        Attributes:
            user_data: the data to create a user
        Methods:
            setup: resets the class attribute back to defaults
    """
    def setUp(self):
        self.user_data = {
            'username': 'TestUser',
            'email': 'test@test.com',
            'password': 'password',
            'first_name': 'first_test',
            'last_name': 'last_test'
        }

        # Create a user
        user = CustomUser.objects.create(
            username=self.user_data['username'],
            email=self.user_data['email'],
            first_name=self.user_data['first_name'],
            last_name=self.user_data['last_name']
        )
        user.set_password(self.user_data['password'])
        user.save()

        # userObject = CustomUser.objects
        # self.client.post(reverse('register_API'), self.user_data, format='json')
        # self.assertTrue(userObject.get(username=self.user_data['username']))

    def test_auth_user_gets_contacts_list(self):
        """Tests to ensure a authenticated user gets their contact list"""
        token = self.client.post(
            reverse('log_API'), {
                'username': self.user_data['username'],
                'password': self.user_data['password'] }).data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get(reverse('contacts_API'))
        self.assertEqual(response.status_code, 200)

    def test_anon_user_gets_rejected(self):
        """
        Tests to ensure a anonymous user gets a non authenticated error
        """
        response = self.client.get(reverse('contacts_API'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data['detail'], ErrorDetail(
            string='Authentication credentials were not provided.',
            code='not_authenticated'))
