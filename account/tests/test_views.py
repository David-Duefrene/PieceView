"""
### test_views.py
### account application views testing suite
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.test import TestCase
from django.urls import reverse

from account.forms import UserRegistrationForm
from account.models import CustomUser

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
    def setUp(self):
        user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )

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
        self.assertTemplateUsed(response, 'registration/register.html')

class UserDashboardTest(TestCase):
    def setUp(self):
        user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )

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
        self.assertTemplateUsed(response, 'user/dashboard.html')

class UserEditTest(TestCase):
    def setUp(self):
        user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )

    def test_redirects_if_not_logged_in(self):
        """
        Tests that the URL actually exists
        """
        response = self.client.get(reverse('edit'))
        self.assertRedirects(response, '/account/login/?next=/account/edit/')

    def test_loggin_uses_correct_template(self):
        """
        Tests that the correct template is rendering
        """
        login = self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get(reverse('edit'))
        self.assertEqual(str(response.context['user']), 'alfred')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/edit.html')

class PeopleListTest(TestCase):
    """
    Test for the People page.
    """
    def setUp(self):
        user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )

    def test_redirects_if_not_logged_in(self):
        """
        Tests that someone who does not have an account gets redirected
        when the try and access the People page.
        """
        response = self.client.get(reverse('user_list'))
        self.assertRedirects(response, '/account/login/?next=/account/people/')

    def test_loggedin_uses_correct_template(self):
        """
        Tests that if the user is logged in is will render the correct template
        for the People page.
        """
        login = self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(str(response.context['user']), 'alfred')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/people.html')

class ProfileDetailTest(TestCase):
    """
    Test for users Profile page.
    """
    def setUp(self):
        user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )

    def test_redirects_if_not_logged_in(self):
        """
        Tests that someone who does not have an account gets redirected
        when the try and access someones Profile page.
        """
        response = self.client.get(reverse('user_detail', args=['alfred']))
        self.assertRedirects(response, '/account/login/?next=/account/people/alfred/')

    def test_loggedin_uses_correct_template(self):
        """
        Tests that if the user is logged in is will render the correct template
        for another users Profile page.
        """
        login = self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get(reverse('user_detail', args=['alfred']))
        self.assertEqual(str(response.context['user']), 'alfred')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')
