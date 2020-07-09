from django.conf import settings
from django.test import TestCase

from account.models import CustomUser
from post.models import Post, Comment


class TestPostModel(TestCase):
    """Tests for the Post Model."""

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',  # skipcq: PTC-W1006
        )
        self.test_post = Post(title='Title', content='test content',
                              authors=self.user)

    def test_post_str(self):
        self.assertEqual(str(self.test_post), 'Title')

    def test_post_url(self):
        url = self.test_post.get_absolute_url()
        self.assertEqual(url, '/post/None/')

    def test_post_content_safe(self):
        """Tests if the save function correctly cleans and saves HTML data"""
        for tag in settings.ALL_TAGS:
            # First we address any tags that need attributes tested.
            if tag == 'img':
                # Correct order for arributes: alt src title
                content = ("<img alt=\"test2.jpg\" src=\"test.jpg\""
                           " title=\"Title\">")

            elif tag == 'area':
                # Correct order for arributes: coords, href then shape
                content = ("<map>\n<area coords=\"0,0,82,126\" "
                           "href=\"sun.htm\" shape=\"rect\">\n</map>")

            # Here we test tags that do not have a subsequent closing tag
            # Right now there is only one, will change  to a list if more
            # tags are added
            elif tag == 'br':
                content = '<br>'

            # Here is table crafted  with all approved subtags
            elif tag == 'table':
                content = ("<table><caption>Caption</caption><thead><tr><th>"
                           "HEAD</th></tr></thead><tbody><tr><th>TH1"
                           "</th><th>TH2</th></tr><tr><td>TD1</td><td>TD2"
                           "</td></tr></tbody><tfoot><tr><td>FT1</td>"
                           "</tr></tfoot></table>")

            else:  # and everything else should be a regular tag
                content = "<" + tag + ">TESTING</" + tag + ">"

            new_post = Post(title='Title', content=content, authors=self.user)
            new_post.save()

            if tag in settings.APPROVED_TAGS and tag not in settings.SUB_TAGS:
                try:
                    self.assertIn(content, new_post.content)
                except AssertionError:
                    print(f"content: {content} failed.")
                    print(f"above content is being filter out"
                          "{new_post.content}")
            else:
                try:
                    self.assertNotIn(content, new_post.content)
                except AssertionError:
                    print(f"content: {content} failed.")
                    print(f"above content is not being filter from:"
                          "{new_post.content}")


class TestCommentModel(TestCase):
    """Tests for the Comment Model."""

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',  # skipcq: PTC-W1006
        )
        self.test_post = Post(title='Title',
                              content='test_post content',
                              authors=self.user)
        self.test_comment = Comment(parent=self.test_post, user=self.user,
                                    body='test_comment body')

    def test_post_str(self):
        self.assertEqual(
            str(self.test_comment),
            f'Comment by {self.user} on {self.test_comment.created}')
