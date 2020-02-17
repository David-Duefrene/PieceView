from django.test import TestCase
from django.urls import reverse

from account.models import CustomUser

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

    def test_next_action(self):
        pop = Populate()
        pop.users(['10'])
        pop.followers(['10', 'alfred'])
        request = {'page_limit': 5, 'page_num': 1, 'user': self.user,
                   'action': 'next'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_followers'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(2, data['new_page'])

    def test_previous_action(self):
        pop = Populate()
        pop.users(['10'])
        pop.followers(['10', 'alfred'])
        request = {'page_limit': 5, 'page_num': 2, 'user': self.user,
                   'action': 'first'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_followers'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(1, data['new_page'])

    def test_first_action(self):
        pop = Populate()
        pop.users(['10'])
        pop.followers(['10', 'alfred'])
        request = {'page_limit': 5, 'page_num': 2, 'user': self.user,
                   'action': 'first'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_followers'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(1, data['new_page'])

    def test_last_action(self):
        pop = Populate()
        pop.users(['10'])
        pop.followers(['10', 'alfred'])
        request = {'page_limit': 5, 'page_num': 2, 'user': self.user,
                   'action': 'last'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_followers'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(2, data['new_page'])

    def test_negative_follower_request(self):
        pop = Populate()
        pop.users(['10'])
        pop.followers(['5', 'alfred'])
        request = {'page_limit': 5, 'page_num': 1, 'user': self.user,
                   'action': 'previous'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_followers'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(1, data['new_page'])

    def test_more_than_total_followers_request(self):
        pop = Populate()
        pop.users(['10'])
        pop.followers(['5', 'alfred'])
        request = {'page_limit': 5, 'page_num': 2, 'user': self.user,
                   'action': 'next'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_followers'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(1, data['new_page'])
