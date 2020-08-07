"""Allows creating a post and a list of posts."""
from collections import OrderedDict

from faker import Faker

from common.create_user import create_user
from post.models import Post


def generate_posts():
    """Will Generate posts for test to use.

    Currently uses a temporary hack
    and saves the username directly as the author instead of the whole
    user object.
    """
    post_list = OrderedDict()
    generator = Faker()
    for post_number in range(5):
        author = create_user()

        title = generator.sentence()
        content = generator.paragraph()
        post = {
            # Saving username directly to authors as a temporary hack
            # Will need to update to properly save User data structure
            'authors': author.username,
            'title': title,
            'content': content
        }
        post_list.update({post_number: OrderedDict(post)})

        Post.objects.create(authors=author, title=title, content=content)

    post_list = OrderedDict(sorted(post_list.items(), reverse=True))
    return post_list


def create_post(user):
    """Will create a post."""
    generator = Faker()
    title = generator.sentence()
    content = generator.paragraph()
    post = Post.objects.create(authors=user, title=title, content=content)
    return post
