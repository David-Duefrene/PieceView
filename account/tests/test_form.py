from django.test import TestCase

from account.forms import *

# UserManager class is not being tested due to it being passed


class TestRegistrationForm(TestCase):
    """Tests for new user registrations form"""
    def test_good_data(self):
        """Test for all data is inputed correctly"""
        # skipcq: PTC-W1006
        form = UserRegistrationForm(data={'password1': "asdVE5asd",
                                          'password2': "asdVE5asd",
                                          'username': "username",
                                          'first_name': "Fname",
                                          'last_name': "Lname",
                                          'email': "mail@mail.com"})

        self.assertTrue(form.is_valid())

    def test_no_username(self):
        """Test to make sure username is required"""
        # skipcq: PTC-W1006
        form = UserRegistrationForm(data={'password1': "asdVE5asd",
                                          'password2': "asdVE5asd",
                                          'username': "",
                                          'first_name': "Fname",
                                          'last_name': "Lname",
                                          'email': "mail@mail.com"})
        self.assertFalse(form.is_valid())

    def test_no_password(self):
        """Tests that the first password fields is required"""
        # skipcq: PTC-W1006
        form = UserRegistrationForm(data={'password1': "",
                                          'password2': "asdVE5asd",
                                          'username': "FAIL",
                                          'first_name': "Fname",
                                          'last_name': "Lname",
                                          'email': "mail@mail.com"})
        self.assertFalse(form.is_valid())

    def test_no_password2(self):
        """Tests the second password field is required"""
        # skipcq: PTC-W1006
        form = UserRegistrationForm(data={'password1': "asdVE5asd",
                                          'password2': "",
                                          'username': "FAIL",
                                          'first_name': "Fname",
                                          'last_name': "Lname",
                                          'email': "mail@mail.com"})
        self.assertFalse(form.is_valid())

    def test_mismatched_passwords(self):
        """Tests to make sure mismatched passwords are rejected"""
        # skipcq: PTC-W1006
        form = UserRegistrationForm(data={'password1': "asdVE5asd",
                                          'password2': "passwordWrong",
                                          'username': "FAIL",
                                          'first_name': "Fname",
                                          'last_name': "Lname",
                                          'email': "mail@mail.com"})
        self.assertFalse(form.is_valid())

    def test_no_first_name(self):
        """Tests to make sure First name is optional"""
        # skipcq: PTC-W1006
        form = UserRegistrationForm(data={'password1': "asdVE5asd",
                                          'password2': "asdVE5asd",
                                          'username': "no_first_name",
                                          'first_name': "",
                                          'last_name': "Lname",
                                          'email': "mail@mail.com"})
        self.assertTrue(form.is_valid())

    def test_no_last_name(self):
        """Tests to make sure Last name is optional"""
        # skipcq: PTC-W1006
        form = UserRegistrationForm(data={'password1': "asdVE5asd",
                                          'password2': "asdVE5asd",
                                          'username': "no_last_name",
                                          'first_name': "Fname",
                                          'last_name': "",
                                          'email': "mail@mail.com"})
        self.assertTrue(form.is_valid())

    def test_no_email(self):
        """Test to make sure email is required"""
        # skipcq: PTC-W1006
        form = UserRegistrationForm(data={'password1': "asdVE5asd",
                                          'password2': "asdVE5asd",
                                          'username': "FAIL",
                                          'first_name': "Fname",
                                          'last_name': "Lname",
                                          'email': ""})
        self.assertFalse(form.is_valid())

    def test_no_data(self):
        """Tests to make sure no data is not accepted"""
        # skipcq: PTC-W1006
        form = UserRegistrationForm(data={'password1': "", 'password2': "",
                                          'username': "", 'first_name': "",
                                          'last_name': "Lname", 'email': ""})
        self.assertFalse(form.is_valid())

    def test_save(self):
        """Test that the form saves"""
        # skipcq: PTC-W1006
        form = UserRegistrationForm(data={'password1': "asdVE5asd",
                                          'password2': "asdVE5asd",
                                          'username': "save",
                                          'first_name': "Fname",
                                          'last_name': "Lname",
                                          'email': "mail@mail.com"})
        form.save(self)
        self.assertTrue(form.is_valid())


class TestUserEditForm(TestCase):
    """Test class for our user edit form"""
    def test_good_data(self):
        """Tests All data is inputed correctly is accepted"""
        form = UserEditForm(data={'first_name': "Fname", 'last_name': "Lname",
                                  'email': "mail@mail.com"})
        self.assertTrue(form.is_valid())

    def test_no_first_name(self):
        """Tests missing first name is accepted"""
        form = UserEditForm(data={'first_name': "", 'last_name': "Lname",
                                  'email': "mail@mail.com"})
        self.assertTrue(form.is_valid())

    def test_no_last_name(self):
        """Tests that missing last name is accepted"""
        form = UserEditForm(data={'first_name': "Fname", 'last_name': "",
                                  'email': "mail@mail.com"})
        self.assertTrue(form.is_valid())

    def test_no_email(self):
        """Test email is required"""
        form = UserEditForm(data={'first_name': "Fname", 'last_name': "Lname",
                                  'email': ""})
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        """Test to see if email is invalid (no @)"""
        form = UserEditForm(data={'first_name': "Fname", 'last_name': "Lname",
                                  'email': "mailcom"})
        self.assertFalse(form.is_valid())
