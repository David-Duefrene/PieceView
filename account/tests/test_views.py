"""
### test_views.py
### account application views testing suite
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.urls import resolve

from selenium import webdriver

from account.models import CustomUser
from account.views import user_login, register, dashboard

import unittest, time

# TODO add to seperate function tests file
class NewVisitorTest(TestCase):
    def setUp(self):
        """
        Set up function for NewVisitorTest
        """
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """
        Tear down function for NewVisitorTest
        """
        self.browser.quit()

    def test_can_create_account(self):
        """
        function to test to see if a new user can create an Account
        """
        # User comes along and hits the page to register a new account
        self.browser.get('http://127.0.0.1:8000/account/register/')
        self.assertIn('Create an Account', self.browser.title)

        username_box = self.browser.find_element_by_id('id_username')
        first_name_box = self.browser.find_element_by_id('id_first_name')
        email_box = self.browser.find_element_by_id('id_email')
        password_box = self.browser.find_element_by_id('id_password')
        pass_verify_box = self.browser.find_element_by_id('id_password2')
        submit_button = self.browser.find_element_by_id('id_submit_button')

        # User fills out the form correctly and hits submit
        username_box.send_keys('coolguy')
        first_name_box.send_keys('Bob')
        email_box.send_keys('coolguy@email.com')
        password_box.send_keys('password')
        pass_verify_box.send_keys('password')
        submit_button.click()
        time.sleep(1)

        # User can now log in
        self.assertIn('Welcome', self.browser.title)
        heading = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Welcome Bob!', heading.text)


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
