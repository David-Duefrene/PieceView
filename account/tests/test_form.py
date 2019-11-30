from django.test import TestCase

from account.forms import LoginForm

class TestLoginForm(TestCase):
	def test_(self):
		form = LoginForm()
		self.assertTrue(form.fields['username'].label == None or form.fields['username'].label == 'username')
