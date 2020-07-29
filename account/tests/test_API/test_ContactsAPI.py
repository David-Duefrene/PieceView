from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

from common.create_user import default_data
from common.create_followers import create_followers, create_following, \
    default_contacts
from account.models import CustomUser


class ContactsAPITest(APITestCase):
    """Test the Contacts API.

        Methods:
            setup: resets the class attribute back to defaults
    """
    def setUp(self):
        create_followers()

    def check(self, data):
        """Checks to see if the type matches default data.

            Params:
                data(dict): the data returned from the server
        """
        # Django returns the followers from newest to oldest
        # So we need to reverse it first
        default_contacts.reverse()
        for index, each in enumerate(data['results']):
            self.assertEqual(
                each['username'], default_contacts[int(index)]['username'])

    def login(self):
        user = CustomUser.objects.get(username=default_data['username'])
        self.client.force_authenticate(user=user)

    def test_auth_user_gets_followers_list_with_no_data(self):
        """Tests to ensure a authenticated user gets their contact list.
           In this test, the user does not send the type to the server.
           The server should default to followers and not give a 500 error.
        """
        self.login()
        response = self.client.get(reverse('contacts_API'))
        self.check(response.data)
        self.assertEqual(response.status_code, 200)

    def test_auth_user_gets_followers_list(self):
        """Tests to ensure a authenticated user gets their contact list.
           In this test, the user sends the followers type to the server.
           The server should return followers list.
        """
        self.login()
        response = self.client.get(
            reverse('contacts_API'), {'type': 'followers'})
        self.assertEqual(response.status_code, 200)
        self.check(response.data)

    def test_bad_type_gets_followers_list(self):
        """Tests to ensure a authenticated user gets their contact list.
           In this test, the user sends the following type to the server.
           The server should return following list.
        """
        self.login()
        response = self.client.get(reverse('contacts_API'), {'type': 'bad'})
        self.assertEqual(response.status_code, 200)
        self.check(response.data)

    def test_anon_user_gets_rejected(self):
        """Tests to ensure a anonymous user gets a non authenticated error
        """
        response = self.client.get(reverse('contacts_API'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data['detail'], ErrorDetail(
            string='Authentication credentials were not provided.',
            code='not_authenticated'))


class FollowersAPITest(APITestCase):
    def setUp(self):
        create_following()

    def test_following(self):
        user = CustomUser.objects.get(username=default_data['username'])
        self.client.force_authenticate(user=user)
        response = self.client.get(
            reverse('contacts_API'), {'type': 'following'})
        self.assertEqual(response.status_code, 200)
        default_contacts.reverse()
        for index, each in enumerate(response.data['results']):
            self.assertEqual(
                each['username'], default_contacts[int(index)]['username'])
