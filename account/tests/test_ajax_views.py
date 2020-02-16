from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from account.models import CustomUser, Contact

import json
from populate import Populate


class GetFollowersTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )

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

    def test_next_set(self):
        pop = Populate()
        pop.users(['12'])
        pop.followers(['12', 'alfred'])

        followers = self.user.followers.all()
        test_list = Contact.paginate.next_set(user=self.user, page_limit=5,
                                              total_followers=25, prev_set=0)

        counter = 0
        for case in test_list:
            self.assertEqual(followers[counter].get_absolute_url(),
                             case['url'])
            counter += 1

        test_list = Contact.paginate.next_set(user=self.user, page_limit=5,
                                              total_followers=25, prev_set=5)
        for case in test_list:
            self.assertEqual(followers[counter].get_absolute_url(),
                             case['url'])
            counter += 1
