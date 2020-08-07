"""Access the post model.

Allows a unauthenticated user to view a list of posts and individual posts.
Allows authenticated users to create a post and modify/delete their own
posts.
"""
from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from faker import Faker
from collections import OrderedDict

from common.create_user import create_user
from common.generate_posts import generate_posts, create_post


class PostListAPITest(APITestCase):
    """Tests the PostListAPI.

    Attributes:
        post_list: a list of test posts
        user: a test user to login with
    """

    def setUp(self):
        """Will set up our tests."""
        self.client = APIClient()
        self.generator = Faker()
        self.post_list = OrderedDict()
        self.user = create_user()

    def test_can_retrieve_posts_while_anon(self):
        """Will ensure a non authenticated account can access the post list."""
        self.post_list = generate_posts()
        response = self.client.get(reverse('post_API'))
        for index, post in enumerate(self.post_list.items()):
            self.assertEqual(
                response.data['results'][index]['title'],
                post[1]['title']
            )
            self.assertEqual(
                response.data['results'][index]['content'], post[1]['content'])
            self.assertEqual(
                response.data['results'][index]['authors']['username'],
                post[1]['authors']
            )

    def test_anon_gets_rejected_when_creating_post(self):
        """Will reject non authenticated user when trying to create a post."""
        response = self.client.post(reverse('post_API'))
        self.assertEqual(response.status_code, 401)

    def test_user_can_create_post_while_authenticated(self):
        """Test to ensure a authenticated user can create a post."""
        self.client.force_authenticate(user=self.user)
        data = {
            'title': self.generator.sentence(),
            'content': self.generator.paragraph()
        }
        response = self.client.post(reverse('post_API'), data)
        self.assertEqual(response.data['status'], 'Success! Post created')

    def test_invalid_title_gets_error(self):
        """Test missing title gets an error."""
        self.client.force_authenticate(user=self.user)

        data = {'content': self.generator.paragraph()}
        response = self.client.post(reverse('post_API'), data)
        self.assertEqual(response.data['Error'], '\'title\' cannot be None')

    def test_invalid_content_gets_error(self):
        """Test missing content gets an error."""
        self.client.force_authenticate(user=self.user)

        data = {'title': self.generator.sentence()}
        response = self.client.post(reverse('post_API'), data)
        self.assertEqual(response.data['Error'], '\'content\' cannot be None')


class PostAPITest(APITestCase):
    """Tests the PostAPI.

    Attributes:
        client: our API client
        post_list: a list of posts for our test
    """

    def setUp(self):
        """Will set up our tests."""
        self.client = APIClient()
        self.post_list = generate_posts()

    def test_can_retrieve_posts_while_anon(self):
        """Test to ensure a non authenticated account can access a post."""
        for index in range(5):
            response = self.client.get(
                reverse('postRUD', kwargs={'pk': index + 1}))

            self.assertEqual(
                response.data['authors']['username'],
                self.post_list[index]['authors']
            )
            self.assertEqual(
                response.data['title'], self.post_list[index]['title'])
            self.assertEqual(
                response.data['content'], self.post_list[index]['content'])

    def test_anon_gets_rejected_when_deleting_a_post(self):
        """Tests to ensure a non authenticated user cannot delete a post."""
        response = self.client.delete(reverse('postRUD', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 401)

    def test_user_cannot_delete_another_users_post(self):
        """Test to ensure a user cannot delete a post that they do not own."""
        user = create_user()
        self.client.force_authenticate(user=user)
        response = self.client.delete(reverse('postRUD', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 403)

    def test_user_can_delete_their_own_post(self):
        """Test to ensure a user can delete their own post."""
        user = create_user()
        self.client.force_authenticate(user=user)
        create_post(user=user)
        response = self.client.delete(reverse('postRUD', kwargs={'pk': 6}))
        self.assertEqual(response.status_code, 204)
