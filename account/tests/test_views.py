"""
### test_views.py
### account application views testing suite
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.test import TestCase

class UserLoginViewTest(TestCase):
    fixtures = ['data_dump.json']

    def is_user_active(self):
        """
        Test to see if the user is active and returns the result
        """
        response = self.client.get('/account/login/')
        self.assertEqual(response.status_code, 200)
        return response.context['user'].is_active

    def test_good_user_login(self):
        """
        Test to see if a good uer/pw will work
        """
        self.assertTrue(self.client.login(username='alfred', password='Hads65ads1'))
        self.assertTrue(self.is_user_active())

    def test_bad_user_login(self):
        """
        Test to see if missing any info on the form will allow a login
        as well as testing a bad user/pw
        """
        # Missing password, good user
        self.assertFalse(self.client.login(username='alfred', password=''))
        self.assertFalse(self.is_user_active())

        # Missing user, good pw
        self.assertFalse(self.client.login(username='', password='Hads65ads1'))
        self.assertFalse(self.is_user_active())

        # Missing both
        self.assertFalse(self.client.login(username='', password=''))
        self.assertFalse(self.is_user_active())

        # Bad LoginForm
        self.assertFalse(self.client.login(username='bad', password='bad'))
        self.assertFalse(self.is_user_active())

    def test_inactive_user_login(self):
        """
        Test to see if a inactive user can login
        """
        # Test inactive user
        self.assertFalse(self.client.login(username='name', password='nfghT56'))
        self.assertFalse(self.is_user_active())
