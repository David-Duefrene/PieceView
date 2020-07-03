from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

from common.create_user import create_user, default_data


class ContactsAPITest(APITestCase):
    """Test the Contacts API.

        Methods:
            setup: resets the class attribute back to defaults
    """
    def setUp(self):
        create_user()

    def test_auth_user_gets_contacts_list(self):
        """Tests to ensure a authenticated user gets their contact list"""
        token = self.client.post(
            reverse('log_API'), {
                'username': default_data['username'],
                'password': default_data['password']}).data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get(reverse('contacts_API'))
        self.assertEqual(response.status_code, 200)

    def test_anon_user_gets_rejected(self):
        """Tests to ensure a anonymous user gets a non authenticated error
        """
        response = self.client.get(reverse('contacts_API'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data['detail'], ErrorDetail(
            string='Authentication credentials were not provided.',
            code='not_authenticated'))
