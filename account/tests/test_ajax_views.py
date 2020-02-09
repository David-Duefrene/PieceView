from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from account.models import CustomUser, Contact

import json


class GetFollowersTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )
        self.user2 = CustomUser.objects.create_user(
            username='Tommy',
            password='Kasdf452'  # skipcq: PTC-W1006
        )
        Contact(from_user=self.user, to_user=self.user2)

    def test_post_rejects_bad_data(self):
        request = {'test': 'bad data'}
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.post(
            reverse('get_followers'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEquals(data['status'], 'Bad Data: 404')

    def test_post_rejects_bad_action(self):
        request = {'page_limit': 5, 'page_num': 1, 'user': self.user,
                   'action': 'bad'}
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.post(
            reverse('get_followers'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEquals(data['status'], 'Bad Request: Bad Action.')
