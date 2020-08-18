from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from common.create_user import create_user


class UserViewSetAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.userList = []
        for each in range(3):
            user = create_user()
            self.userList.append(user.username)

    def test_able_to_retrieve_user_list(self):
        result = self.client.get(reverse('api_account'))
        for user in result.data['results']:
            self.assertTrue(user['username'] in self.userList)
