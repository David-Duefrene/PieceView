"""
### test_admin.py
### account application testing suite for admin functions
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.contrib.admin.sites import AdminSite
from django.test import TestCase, Client

from account.models import CustomUser

class TestCustomerUserAdmin(TestCase):

    def setUp(self):
        self.client = Client()
        user = CustomUser.objects.create_superuser(
            username='admin',
            password='password',
        )

    def test_good_admin_login(self):
        """
        Tests to see if admin can login with good user/pw
        """
        c = Client()
        self.assertTrue(c.login(username='admin', password='password'))
