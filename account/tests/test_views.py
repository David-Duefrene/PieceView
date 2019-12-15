"""
### test_views.py
### account application views testing suite
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.test import TestCase, Client

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
        Test to see if a good uer/pw will redirect
        """
        c = Client()
        response = c.post('/account/login/', {'username': 'alfred',
                            'password': 'Hads65ads1'}, follow=True)
        self.assertTrue(response.status_code, 200)
        self.assertIn(bytes("Hello Alfred", 'utf-8'), response.content)

    def test_login_view(self):
        response = self.client.get('/account/login/')
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_bad_user_login(self):
        """
        Test to see if missing any info on the form will allow a login
        as well as testing a bad user/pw
        """
        # Testing missing username
        c = Client()
        response = c.post('/account/login/', {'username': '',
                            'password': 'Hads65ads1'})
        self.assertIn(bytes("<ul class=\"errorlist\"><li>This field is required.</li></ul>\n<p><label for=\"id_username\">Username:</label>",
                            'utf-8'), response.content)

        # Missing password, good user
        c = Client()
        response = c.post('/account/login/', {'username': 'alfred',
                            'password': ''})
        self.assertIn(bytes("<ul class=\"errorlist\"><li>This field is required.</li></ul>\n<p><label for=\"id_password\">Password:</label>",
                            'utf-8'), response.content)

        # Testing missing bioth fields
        c = Client()
        response = c.post('/account/login/', {'username': '', 'password': ''})
        self.assertIn(bytes("<ul class=\"errorlist\"><li>This field is required.</li></ul>\n<p><label for=\"id_password\">Password:</label>",
                            'utf-8'), response.content)
        self.assertIn(bytes("<ul class=\"errorlist\"><li>This field is required.</li></ul>\n<p><label for=\"id_username\">Username:</label>",
                            'utf-8'), response.content)

        # Test bad login info
        c = Client()
        response = c.post('/account/login/', {'username': 'bad', 'password': 'bad'})
        self.assertIn(bytes("<ul class=\"errorlist nonfield\"><li>Please enter a correct username and password. Note that both fields may be case-sensitive.</li></ul>",
                            'utf-8'), response.content)

    def test_inactive_user_login(self):
        """
        Test to see if a inactive user can login
        """
        c = Client()
        response = c.post('/account/login/', {'username': 'name', 'password': 'nfghT56'})
        self.assertIn(bytes("<ul class=\"errorlist nonfield\"><li>Please enter a correct username and password. Note that both fields may be case-sensitive.</li></ul>",
                            'utf-8'), response.content)

class UserDashboardTest(TestCase):
    fixtures = ['data_dump.json']

    def test_user_dashboard(self):
        """
        Tests the user dashboard
        """
        self.assertTrue(self.client.login(username='alfred', password='Hads65ads1'))
        request = self.client.get('/account/')
        self.assertTemplateUsed(request, 'account/dashboard.html')
