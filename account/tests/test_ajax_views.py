from django.test import TestCase
from django.urls import reverse

from account.models import CustomUser

import json
from populate import Populate


class GetUsersTest(TestCase):
    ''' Class for testing the GetUsers ajax view.'''
    def setUp(self):
        ''' Creates a user as self.user.'''
        self.user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )

    def test_post_rejects_bad_data(self):
        ''' Test to make sure view rejects bad data.'''
        request = {'test': 'bad data'}
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.post(
            reverse('get_users'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data['status'], 'Bad Data: 404')

    def test_post_rejects_bad_action(self):
        ''' Makes sure the view rejects bad actions.'''
        request = {'page_limit': 5, 'page_num': 1, 'user': self.user,
                   'action': 'bad', 'request_type': 'followers'}
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.post(
            reverse('get_users'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data['status'], 'Bad Request: Bad Action.')

    def test_post_rejects_bad_request_type(self):
        ''' Makes sure the view rejects bad request types.'''
        request = {'page_limit': 5, 'page_num': 1, 'user': self.user,
                   'action': 'first', 'request_type': 'bad'}
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.post(
            reverse('get_users'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data['status'], 'Bad request_type')

    def test_following_request_accepted(self):
        ''' Make sure the view accepts following as a request_type.'''
        pop = Populate()
        pop.users(['10'])
        pop.following(['10', 'alfred'])
        request = {'page_limit': 5, 'page_num': 2, 'user': self.user,
                   'action': 'first', 'request_type': 'following'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_users'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['following']), 'message')
        self.assertEqual(1, data['new_page'])

    def test_next_action(self):
        ''' Make sure the view get the next page correctly.'''
        pop = Populate()
        pop.users(['10'])
        pop.followers(['10', 'alfred'])
        request = {'page_limit': 5, 'page_num': 1, 'user': self.user,
                   'action': 'next', 'request_type': 'followers'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_users'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(2, data['new_page'])

    def test_previous_action(self):
        ''' Make sure the view get the previous page correctly.'''
        pop = Populate()
        pop.users(['10'])
        pop.followers(['10', 'alfred'])
        request = {'page_limit': 5, 'page_num': 2, 'user': self.user,
                   'action': 'first', 'request_type': 'followers'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_users'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(1, data['new_page'])

    def test_first_action(self):
        ''' Make sure the view get the first page correctly.'''
        pop = Populate()
        pop.users(['10'])
        pop.followers(['10', 'alfred'])
        request = {'page_limit': 5, 'page_num': 2, 'user': self.user,
                   'action': 'first', 'request_type': 'followers'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_users'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(1, data['new_page'])

    def test_last_action(self):
        ''' Make sure the view get the last page correctly.'''
        pop = Populate()
        pop.users(['10'])
        pop.followers(['10', 'alfred'])
        request = {'page_limit': 5, 'page_num': 2, 'user': self.user,
                   'action': 'last', 'request_type': 'followers'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_users'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(2, data['new_page'])

    def test_negative_follower_request(self):
        ''' Make sure the view does not attempt to get a 0 or negative page.'''
        pop = Populate()
        pop.users(['10'])
        pop.followers(['5', 'alfred'])
        request = {'page_limit': 5, 'page_num': 1, 'user': self.user,
                   'action': 'previous', 'request_type': 'followers'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_users'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(1, data['new_page'])

    def test_more_than_total_followers_request(self):
        '''
        Make sure the view does not attempt to get a page past whats available.
        '''
        pop = Populate()
        pop.users(['10'])
        pop.followers(['5', 'alfred'])
        request = {'page_limit': 5, 'page_num': 2, 'user': self.user,
                   'action': 'next', 'request_type': 'followers'}
        self.client.login(username='alfred', password='Hads65ads1')

        response = self.client.post(
            reverse('get_users'),
            request,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual('OK', data['status'])
        self.assertEqual(5, len(data['followers']), 'message')
        self.assertEqual(1, data['new_page'])
