"""
### test_admin.py
### account application testing suite for admin functions
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.contrib.admin.sites import AdminSite
from django.test import TestCase, Client

class TestCustomerUserAdmin(TestCase):
    fixtures = ['data_dump.json']

    def test_good_admin_login(self):
        """
        Tests to see if admin can login with good user/pw
        """
        c = Client()
        c.login(username='admin', password='password')
