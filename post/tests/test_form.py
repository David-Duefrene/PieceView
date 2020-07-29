from django.test import TestCase

from post.forms import PostCreateForm, CommentForm


class TestPostCreateForm(TestCase):
    """ Tests for PostCreateForm. """

    def test_good_data(self):
        """Tests if all data is correct."""
        form = PostCreateForm(data={'title': 'test title',
                                    'content': 'test_content'})
        self.assertTrue(form.is_valid())

    def test_no_title(self):
        """Tests if  user forgets a title."""
        form = PostCreateForm(data={'title': '', 'content': 'test_content'})
        self.assertFalse(form.is_valid())

    def test_no_content(self):
        """Tests if  user forgets the content."""
        form = PostCreateForm(data={'title': 'test title', 'content': ''})
        self.assertFalse(form.is_valid())

    def test_no_data(self):
        """Tests if  user forgets the content."""
        form = PostCreateForm(data={'title': '', 'content': ''})
        self.assertFalse(form.is_valid())


class TestCommentForm(TestCase):
    """ Tests for CommentForm """

    def test_good_data(self):
        """ Tests if all data is correct. """
        form = CommentForm(data={'body': 'Test_Body'})
        self.assertTrue(form.is_valid())

    def test_no_body(self):
        """Tests of user attempts to submit a comment with no body"""
        form = CommentForm(data={'body': ''})
        self.assertFalse(form.is_valid())
