from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from account.models import CustomUser


class UserLoginViewTest(TestCase):
    """Tests for our login view"""
    def test_view_url_exists_at_desired_location(self):
        """Tests that the URL actually exists"""
        response = self.client.get('/account/login/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """Tests that the correct template is rendering"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


class UserLogoutViewTest(TestCase):
    """ Tests for user logging out view"""
    def setUp(self):
        CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )

    def test_view_url_exists_at_desired_location(self):
        """Tests that the URL actually exists"""
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get('/account/logout/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """Tests that the correct template is rendering"""
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/logged_out.html')


class UserRegistrationViewTest(TestCase):
    """Tests to ensure Registration view is correct"""
    def test_view_url_exists_at_desired_location(self):
        """Tests that the URL actually exists"""
        response = self.client.get('/account/register/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """Tests that the correct template is rendering"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')


class UserDashboardTest(TestCase):
    """ View test for our user dashboard"""
    def setUp(self):
        CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )

    def test_redirects_if_not_logged_in(self):
        """Tests that the URL actually exists"""
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/account/login/?next=/account/')

    def test_loggin_uses_correct_template(self):
        """Tests that the correct template is rendering"""
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/dashboard.html')


class UserEditTest(TestCase):
    """ Test for the user edit view"""
    def setUp(self):
        CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )
        CustomUser.objects.create_user(
            username='Tommy',
            password='Kasdf452'
        )

    def test_redirects_if_not_logged_in(self):
        """Tests that a edit url will redirect if no user is logged in."""
        response = self.client.get(reverse('edit', kwargs={'pk': 1}))
        self.assertRedirects(response, '/account/login/?next=/account/edit/1/')

    def test_loggin_uses_correct_template(self):
        """Tests that the correct template is being rendered"""
        self.client.login(username='alfred', password='Hads65ads1')
        # DeepSource flags pk as un pythonic. Although correct ignoring it
        # as well as the _default_manager protected flag, ignoring for tests
        # skipcq: PYL-C0103, PYL-W0212
        pk = get_user_model()._default_manager.get(username__exact='alfred').pk
        response = self.client.get(reverse('edit', kwargs={'pk': pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/edit.html')

    def test_user_can_only_edit_own_profile(self):
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get(reverse('edit', kwargs={'pk': 2}))
        self.assertTemplateUsed(response, 'user/dashboard.html')


class PeopleListTest(TestCase):
    """Test for the People view."""
    def setUp(self):
        CustomUser.objects.create_user(
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
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/people.html')


class ProfileDetailTest(TestCase):
    """Test for users Profile Detail view."""
    def setUp(self):
        CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )
        CustomUser.objects.create_user(
            username='Tommy',
            password='Kasdf452'
        )

    def test_redirects_if_not_logged_in(self):
        """
        Tests that someone who does not have an account gets redirected
        to a login when they try and access someone's Profile page.
        """
        response = self.client.get(reverse('user_detail', args=['alfred']))
        self.assertRedirects(response,
                             '/account/login/?next=/account/people/alfred/')

    def test_loggedin_uses_correct_template(self):
        """
        Tests that if the user is logged in is will render the correct template
        for another users Profile page.
        """
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get(reverse('user_detail', args=['alfred']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')

    def test_user_can_follow(self):
        """
        Test to see if a user has a follow button if they are not following a
        Profile
        """
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.post(reverse('user_follow'),
                                    data={'id': 2, 'action': 'follow'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(b'{"status": "follow"}', response.content)

    def test_user_can_unfollow(self):
        """Tests to make sure a user can unfollow another user"""
        self.client.login(username='alfred', password='Hads65ads1')
        # skipcq FLK-E302
        button = '<button data-id="2" data-action="follow"\n            class="btn btn-primary btn-lg follow">Follow'
        follow = self.client.post(reverse('user_follow'),
                                  data={'id': 2, 'action': 'follow'},
                                  HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(b'{"status": "follow"}', follow.content)

        unfollow = self.client.post(reverse('user_follow'),
                                    data={'id': 2, 'action': 'unfollow'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(b'{"status": "unfollow"}', unfollow.content)


class FollowUserTest(TestCase):
    """Tests for following users"""
    def setUp(self):
        CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )
        CustomUser.objects.create_user(
            username='Tommy',
            password='Kasdf452'
        )

    def test_can_follow_user(self):
        """Tests that a logged in user can follow another user"""
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.post(reverse('user_follow'),
                                    data={'id': 2, 'action': 'follow'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'{"status": "follow"}', response.content)

    def test_user_can_unfollow(self):
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.post(reverse('user_follow'),
                                    data={'id': 2, 'action': 'unfollow'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'{"status": "unfollow"}', response.content)

    def test_unauthinticated_gets_rejected(self):
        """Tests a unauthenticated user gets redirected to log in screen"""
        response = self.client.post(reverse('user_follow'),
                                    data={'id': 2, 'action': 'follow'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True)
        self.assertIn(b"Please use the follwoing form to log-in:",
                      response.content)

    def test_http_request_rejected(self):
        response = self.client.post(reverse('user_follow'),
                                    data={'id': 2, 'action': 'follow'})
        self.assertEqual(response.status_code, 400)
