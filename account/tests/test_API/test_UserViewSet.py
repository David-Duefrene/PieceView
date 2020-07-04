from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from common.create_user import create_user


class UserViewSetAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.data1 = {
            'username': 'TestUser1', 'email': 'test1@test.com',
            'password': 'password1', 'first_name': 'first_test1',
            'last_name': 'last_test1'
        }
        self.data2 = {
            'username': 'TestUser2', 'email': 'test2@test.com',
            'password': 'password2', 'first_name': 'first_test2',
            'last_name': 'last_test2'
        }
        self.data3 = {
            'username': 'TestUser3', 'email': 'test3@test.com',
            'password': 'password3', 'first_name': 'first_test3',
            'last_name': 'last_test3'
        }

        create_user(self.data1)
        create_user(self.data2)
        create_user(self.data3)

    def test_able_to_retrieve_user_list(self):
        self.client.get(reverse('api_account'))
