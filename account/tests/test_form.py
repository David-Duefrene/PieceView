"""
### test_forms.py
### account application forms testing suite
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.test import TestCase

from account.forms import LoginForm, UserRegistrationForm

class TestLoginForm(TestCase):
	# Form requires both user & PW
	def test_good_data(self):
		form = LoginForm(data={'username': "name", 'password': "password"})
		self.assertTrue(form.is_valid())

	# And should return False if missing either one
	def test_no_username(self):
		form = LoginForm(data={'username': "", 'password': "password"})
		self.assertFalse(form.is_valid())

	def test_no_passwords(self):
		form = LoginForm(data={'username': "name", 'password': ""})
		self.assertFalse(form.is_valid())
	# or if missing both
	def test_no_data(self):
		form = LoginForm(data={'username': "", 'password': ""})
		self.assertFalse(form.is_valid())

# UserManager class is not being tested due to it being passed

class TestRegistrationForm(TestCase):
	# All data is inputed correctly
	def test_good_data(self):
		form = UserRegistrationForm(data={'password': "password", 'password2': "password",
				'username': "username", 'first_name': "name", 'email': "mail@mail.com"})

		self.assertTrue(form.is_valid())

	# No username, username should be required
	def test_no_username(self):
		form = UserRegistrationForm(data={'password': "password", 'password2': "password",
				'username': "", 'first_name': "name", 'email': "mail@mail.com"})
		self.assertFalse(form.is_valid())

	# Tests the first password field, should return False
	def test_no_password(self):
		form = UserRegistrationForm(data={'password': "pass", 'password2': "password",
				'username': "username", 'first_name': "name", 'email': "mail@mail.com"})
		self.assertFalse(form.is_valid())

	# Tests the second password field, also should return False
	def test_no_password2(self):
		form = UserRegistrationForm(data={'password': "password", 'password2': "",
				'username': "username", 'first_name': "name", 'email': "mail@mail.com"})
		self.assertFalse(form.is_valid())

	# Testing PW mismatch, should return False
	def test_mismatched_passwords(self):
		form = UserRegistrationForm(data={'password': "password", 'password2': "passwordWrong",
				'username': "username", 'first_name': "name", 'email': "mail@mail.com"})
		self.assertFalse(form.is_valid())

	# No first name inputted, Fist and Last name are optional and should still return true
	def test_no_first_name(self):
		form = UserRegistrationForm(data={'password': "password", 'password2': "password",
				'username': "username", 'first_name': "", 'email': "mail@mail.com"})
		self.assertTrue(form.is_valid())

	# TODO add last name test here

	# User forgot email, email should be required
	def test_no_email(self):
		form = UserRegistrationForm(data={'password': "password", 'password2': "password",
				'username': "username", 'first_name': "name", 'email': ""})
		self.assertFalse(form.is_valid())

	def test_no_data(self):
		form = UserRegistrationForm(data={'password': "", 'password2': "",
				'username': "", 'first_name': "", 'email': ""})
		self.assertFalse(form.is_valid())

	def test_save(self):
		form = UserRegistrationForm(data={'password': "password", 'password2': "password",
				'username': "username", 'first_name': "name", 'email': "mail@mail.com"})
		form.save(self)
		self.assertTrue(form.is_valid())
