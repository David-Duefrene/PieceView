from django.test import TestCase
from django.urls import reverse

from account.models import CustomUser
from post.models import Post


class TestPostCreateView(TestCase):
    """Tests for the Post Create View"""
    def setUp(self):
        CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',  # skipcq: PTC-W1006
        )

    def test_view_url_exists_at_desired_location(self):
        """Tests that the URL actually exists"""
        # skipcq: PTC-W1006
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get('/post/create/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """Tests that the correct template is rendering"""
        # skipcq: PTC-W1006
        self.client.login(username='alfred', password='Hads65ads1')
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/create_post.html')

    def test_redirects_if_not_logged_in(self):
        """Tests that the URL redirects if user is not logged in."""
        response = self.client.get(reverse('create_post'))
        self.assertRedirects(response, '/account/login/?next=/post/create/')


class TestPostDetailView(TestCase):
    """Tests for the Post Detail View"""
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',  # skipcq: PTC-W1006
        )
        self.client.login(username='alfred', password='Hads65ads1')

        self.test_post = self.client.post(reverse('create_post'), data={
            'title': "Title",
            'content': 'content',
            'authors': self.user,
        })
        self.client.logout()

    def test_view_url_exists_at_desired_location(self):
        """Tests that the URL actually exists"""
        response = self.client.get(reverse('post_detail', args=['1']))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """Tests that the correct template is rendering"""
        response = self.client.get(reverse('post_detail', args=['1']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/post_detail.html')


class TestPostListView(TestCase):
    """Tests for the Post List View"""
    def test_view_url_exists_at_desired_location(self):
        """Tests that the URL actually exists"""
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """Tests that the correct template is rendering"""
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/post_list.html')
