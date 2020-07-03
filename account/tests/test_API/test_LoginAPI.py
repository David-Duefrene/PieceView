from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

from common.create_user import create_user, default_data


class LoginAPITest(APITestCase):
    """Tests the Login API.

        Methods:
            setUp(self): creates a user for every test
            login(self): logs the user in with self.login_data
    """
    def setUp(self):
        self.login_data = {
            'username': default_data['username'],
            'password': default_data['password']
        }
        create_user()

    def login(self):
        """ Logs the user in with self.login_data.

            Returns the server response
        """
        return self.client.post(reverse('log_API'), self.login_data)

    def test_valid_credentials_can_login(self):
        """Tests to make sure good username and passord returns a HTTP 200 code,
           a user object, and a token.
        """
        response = self.login()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['user'])
        self.assertTrue(response.data['token'])

    def test_bad_username_is_rejected(self):
        """Test to make sure a bad username is rejected.
        """
        self.login_data['username'] = 'bad'
        response = self.login()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data['non_field_errors'],
            [ErrorDetail(string='Incorrect Credentials', code='invalid')]
        )

    def test_bad_password_is_rejected(self):
        """Test to make sure a bad password is rejected.
        """
        self.login_data['password'] = 'bad'
        response = self.login()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data['non_field_errors'],
            [ErrorDetail(string='Incorrect Credentials', code='invalid')]
        )

    def test_no_username_is_rejected(self):
        """Test to make sure no username is rejected.
        """
        self.login_data['username'] = ''
        response = self.login()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, {
                'username':
                [ErrorDetail(
                    string='This field may not be blank.', code='blank'
                )]
            }
        )

    def test_no_password_is_rejected(self):
        """Test to make sure no password is rejected.
        """
        self.login_data['password'] = ''
        response = self.login()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, {
                'password':
                [ErrorDetail(
                    string='This field may not be blank.', code='blank'
                )]
            }
        )
