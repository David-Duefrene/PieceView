from django.urls import reverse

from rest_framework.test import APITestCase

from faker import Faker
from collections import OrderedDict

from account.models import CustomUser
from post.models import Post


class PostAPITest(APITestCase):
    """Tests the PostAPI.

        Attributes:
            post_data: data for a test post
            user_data: data to generate a user
            login_data: data to log a user in

        Methods:
            setup: resets the class attribute back to defaults
            generate_posts: helper function to allow tests to generate posts

        Test List:
            test_can_retrieve_posts_while_anon
    """

    def setUp(self):
        self.generator = Faker()
        self.post_list = OrderedDict()

    def generate_posts(self, number_of_posts=5):
        """Generates posts for test to use. Currently uses a temporary hack
            and saves the username directly as the author instead of the whole
            user object.

            arguments:
                number_of_posts: OPTIONAL, uses 5 as default, number of posts
                    to create
        """
        for post_number in range(number_of_posts):
            full_name = self.generator.name()
            full_name = full_name.split()
            username = full_name[0][0] + full_name[1]

            author = CustomUser.objects.create(username=username)
            author.set_password('password')
            author.save()

            title = self.generator.sentence()
            content = self.generator.paragraph()
            post = {
                # Saving username directly to authors as a temporary hack
                # Will need to update to properly save User data structure
                'authors': author.username,  # post_number + 1,
                'title': title,
                'content': content
            }
            self.post_list.update({post_number: OrderedDict(post)})

            Post.objects.create(
                authors=author, title=title, content=content)

        self.post_list = OrderedDict(sorted(
            self.post_list.items(), reverse=True))

    def test_can_retrieve_posts_while_anon(self):
        """Test to ensure a non authenticated account can access the
            post list.
        """
        self.generate_posts(5)
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
        response = self.client.post(reverse('post_API'))
        self.assertEqual(response.status_code, 401)

    def test_user_can_create_post_while_authenticated(self):
        full_name = self.generator.name()
        full_name = full_name.split()
        username = full_name[0][0] + full_name[1]

        test_user = CustomUser.objects.create(username=username)
        test_user.set_password('password')
        test_user.save()
        token = self.client.post(
            reverse('log_API'), {
                'username': username,
                'password': 'password'},
            format='json').data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        data = {
            'title': self.generator.sentence(),
            'content': self.generator.paragraph()
        }
        response = self.client.post(reverse('post_API'), data)
        self.assertEqual(response.data['status'], 'Success! Post created')

    def test_invalid_title_gets_error(self):
        full_name = self.generator.name()
        full_name = full_name.split()
        username = full_name[0][0] + full_name[1]

        test_user = CustomUser.objects.create(username=username)
        test_user.set_password('password')
        test_user.save()
        token = self.client.post(
            reverse('log_API'), {
                'username': username,
                'password': 'password'},
            format='json').data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        data = {'content': self.generator.paragraph()}
        response = self.client.post(reverse('post_API'), data)
        self.assertEqual(response.data['Error'], '\'title\' cannot be None')

    def test_invalid_content_gets_error(self):
        full_name = self.generator.name()
        full_name = full_name.split()
        username = full_name[0][0] + full_name[1]

        test_user = CustomUser.objects.create(username=username)
        test_user.set_password('password')
        test_user.save()
        token = self.client.post(
            reverse('log_API'), {
                'username': username,
                'password': 'password'},
            format='json').data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        data = {'title': self.generator.sentence()}
        response = self.client.post(reverse('post_API'), data)
        self.assertEqual(response.data['Error'], '\'content\' cannot be None')
