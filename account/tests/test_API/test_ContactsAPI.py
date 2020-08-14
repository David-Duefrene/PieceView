from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

from common.create_followers import create_followers, create_following
from account.models import CustomUser


class ContactsAPITest(APITestCase):
    """Test the Contacts API.

        Methods:
            check: checks to see if out contacts matches.
    """
    def setUp(self):
        data = create_followers()
        self.user = data['user']
        self.contacts = data['contacts']

    def check(self, data):
        """Checks to see if the type matches default data.

            Params:
                data(dict): the data returned from the server
        """
        for index, each in enumerate(data['results']):
            self.assertTrue(each['username'] in self.contacts)

    def login(self):
        user = CustomUser.objects.get(username=self.user.username)
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
        data = create_following()
        self.user = data['user']
        self.contacts = data['contacts']

    def test_following(self):
        user = CustomUser.objects.get(username=self.user.username)
        self.client.force_authenticate(user=user)
        response = self.client.get(
            reverse('contacts_API'), {'type': 'following'})
        self.assertEqual(response.status_code, 200)
        for index, each in enumerate(response.data['results']):
            self.assertTrue(each['username'] in self.contacts)
