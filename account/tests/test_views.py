"""
### test_views.py
### account application views testing suite
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.test import TestCase
from django.urls import reverse

from account.forms import UserRegistrationForm

class UserLoginViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        """
        Tests that the URL actually exists
        """
        response = self.client.get('/account/login/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """
        Tests that the correct template is rendering
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

class UdserLogoutViewTest(TestCase):
    fixtures = ['data_dump.json']

    def test_view_url_exists_at_desired_location(self):
        """
        Tests that the URL actually exists
        """
        login = self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get('/account/logout/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """
        Tests that the correct template is rendering
        """
        login = self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/logged_out.html')

class UserRegistrationViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        """
        Tests that the URL actually exists
        """
        response = self.client.get('/account/register/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """
        Tests that the correct template is rendering
        """
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')

class UserDashboardTest(TestCase):
    fixtures = ['data_dump.json']

    def test_redirects_if_not_logged_in(self):
        """
        Tests that the URL actually exists
        """
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/account/login/?next=/account/')

    def test_loggin_uses_correct_template(self):
        """
        Tests that the correct template is rendering
        """
        login = self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(str(response.context['user']), 'alfred')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/dashboard.html')
