from django.test import TestCase

from account.forms import *

# UserManager class is not being tested due to it being passed


class TestRegistrationForm(TestCase):
    """Tests for new user registrations form"""
    def test_good_data(self):
        """Test for all data is inputed correctly"""
        form = UserRegistrationForm(data={'password': "password",
                                          'password2': "password",
                                          'username': "username",
                                          'first_name': "name",
                                          'email': "mail@mail.com"})

        self.assertTrue(form.is_valid())

    def test_no_username(self):
        """Test to make sure username is required"""
        form = UserRegistrationForm(data={'password': "password",
                                          'password2': "password",
                                          'username': "",
                                          'first_name': "name",
                                          'email': "mail@mail.com"})
        self.assertFalse(form.is_valid())

    def test_no_password(self):
        """Tests that the first password fields is required"""
        form = UserRegistrationForm(data={'password': "pass",
                                          'password2': "password",
                                          'username': "username",
                                          'first_name': "name",
                                          'email': "mail@mail.com"})
        self.assertFalse(form.is_valid())

    def test_no_password2(self):
        """Tests the second password field is required"""
        form = UserRegistrationForm(data={'password': "password",
                                          'password2': "",
                                          'username': "username",
                                          'first_name': "name",
                                          'email': "mail@mail.com"})
        self.assertFalse(form.is_valid())

    def test_mismatched_passwords(self):
        """Tests to make sure mismatched passwords are rejected"""
        form = UserRegistrationForm(data={'password': "password",
                                          'password2': "passwordWrong",
                                          'username': "username",
                                          'first_name': "name",
                                          'email': "mail@mail.com"})
        self.assertFalse(form.is_valid())

    def test_no_first_name(self):
        """Tests to make sure First name is optional"""
        form = UserRegistrationForm(data={'password': "password",
                                          'password2': "password",
                                          'username': "username",
                                          'first_name': "",
                                          'email': "mail@mail.com"})
        self.assertFalse(form.is_valid())

    # TODO add last name test here

    def test_no_email(self):
        """Test to make sure email is required"""
        form = UserRegistrationForm(data={'password': "password",
                                          'password2': "password",
                                          'username': "username",
                                          'first_name': "name", 'email': ""})
        self.assertFalse(form.is_valid())

    def test_no_data(self):
        """Tests to make sure no data is not accepted"""
        form = UserRegistrationForm(data={'password': "", 'password2': "",
                                          'username': "", 'first_name': "",
                                          'email': ""})
        self.assertFalse(form.is_valid())

    def test_save(self):
        """Test that the form saves"""
        form = UserRegistrationForm(data={'password': "password",
                                          'password2': "password",
                                          'username': "username",
                                          'first_name': "name",
                                          'email': "mail@mail.com"})
        form.save(self)
        self.assertTrue(form.is_valid())


class TestUserEditForm(TestCase):
    """Test class for our user edit form"""
    def test_good_data(self):
        """Tests All data is inputed correctly is accepted"""
        form = UserEditForm(data={'first_name': "name", 'last_name': "named",
                                  'email': "mail@mail.com"})
        self.assertTrue(form.is_valid())

    def test_no_first_name(self):
        """Tests missing first name is rejected"""
        form = UserEditForm(data={'first_name': "", 'last_name': "named",
                                  'email': "mail@mail.com"})
        self.assertFalse(form.is_valid())

    def test_no_last_name(self):
        """Tests that missing last name is accepted"""
        form = UserEditForm(data={'first_name': "name", 'last_name': "",
                                  'email': "mail@mail.com"})
        self.assertTrue(form.is_valid())

    def test_no_email(self):
        """Test email is required"""
        form = UserEditForm(data={'first_name': "name", 'last_name': "named",
                                  'email': ""})
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        """Test to see if email is invalid (no @)"""
        form = UserEditForm(data={'first_name': "name", 'last_name': "named",
                                  'email': "mailcom"})
        self.assertFalse(form.is_valid())
