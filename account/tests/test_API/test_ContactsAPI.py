from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

from account.models import CustomUser


class ContactsAPITest(APITestCase):
    """Test the Contacts API"""
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

    def test_auth_user_gets_contacts_list(self):
        """Tests to ensure a authenticated user gets their contact list"""
        token = self.client.post(
            reverse('log_API'),
            {
                'username': self.data['username'],
                'password': self.data['password']
            },
        ).data['token']
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
