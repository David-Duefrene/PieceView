from django.test import TestCase

from account.forms import *

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
		self.assertFalse(form.is_valid())

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

class TestUserEditForm(TestCase):
	# All data is inputed correctly
	def test_good_data(self):
		form = UserEditForm(data={'first_name': "name", 'last_name': "named", 'email': "mail@mail.com"})
		self.assertTrue(form.is_valid())

	# Test no first name
	def test_no_first_name(self):
		form = UserEditForm(data={'first_name': "", 'last_name': "named", 'email': "mail@mail.com"})
		self.assertFalse(form.is_valid())

	# Test no last name
	def test_no_last_name(self):
		form = UserEditForm(data={'first_name': "name", 'last_name': "", 'email': "mail@mail.com"})
		self.assertTrue(form.is_valid())

	# Test no email
	def test_no_email(self):
		form = UserEditForm(data={'first_name': "name", 'last_name': "named", 'email': ""})
		self.assertFalse(form.is_valid())

	# Test invalid email
	def test_invalid_email(self):
		form = UserEditForm(data={'first_name': "name", 'last_name': "named", 'email': "mailcom"})
		self.assertFalse(form.is_valid())
