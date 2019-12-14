"""
### test_user_perspective.py
### account application functional testing suite
### tests user perspective
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.test import TestCase

from selenium import webdriver

import time

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
