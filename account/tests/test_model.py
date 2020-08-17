"""Tests the User and Contact models"""
import os
from django.test import TestCase

from account.models import CustomUser, Contact


class CustomUserModelTest(TestCase):
    """Tests the CustomUser model"""

    def setUp(self):
        """Create 1 user"""
        self.user = CustomUser.objects.create_user(
            username='alfred', password='Hads65ads1',  # skipcq: PTC-W1006
        )

    def test_default_photo_url(self):
        """Test for default photo url"""
        self.assertEqual(
            f'{os.environ.get("STATIC_URL")}static/icons/no-picture.jpg',
            self.user.photo_link)

    def test_custom_photo_link(self):
        """Test for correct URL if the user uploads a photo link"""
        self.user.photo_link = 'test.com/photo'
        self.assertEqual('test.com/photo', self.user.photo_url)


class ContactModelTest(TestCase):
    """Tests the Contact model

    Methods:
        setUp(self): creates 2 users every test
    """

    def setUp(self):
        """Create 2 users"""
        self.user = CustomUser.objects.create_user(
            username='alfred', password='Hads65ads1',  # skipcq: PTC-W1006
        )
        self.user2 = CustomUser.objects.create_user(
            username='Tommy', password='Kasdf452'  # skipcq: PTC-W1006
        )

    def test_follow(self):
        """Test to make sure str method functions with follow"""
        follow = Contact(from_user=self.user, to_user=self.user2)
        self.assertEqual('alfred follows Tommy', str(follow))
