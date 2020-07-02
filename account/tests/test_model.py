from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

import os

from account.models import CustomUser, Contact


class CustomUserModelTest(TestCase):
    """Tests the CustomUser model.

        Attributes:
        Methods:
    """
    def test_default_photo_url(self):
        """Tests the photo url"""
        test_user = CustomUser()
        self.assertEqual("/static/icons/no-picture.jpg", test_user.photo_url)

    def test_custom_photo_url(self):
        """Tests correct url if a user uploads there own photo"""
        # photo should be in /PieceView/account/tests
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  'albert-einstien.jpg')
        test_user = CustomUser()
        with open(image_path, 'rb') as file:
            test_user.photo = SimpleUploadedFile(name='test_image.jpg',
                                                 content=file.read(),
                                                 content_type='image/jpeg')

            self.assertEqual("/media/test_image.jpg", test_user.photo_url)


class ContactModelTest(TestCase):
    """Tests the Contact model"""
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='alfred', password='Hads65ads1',  # skipcq: PTC-W1006
        )
        self.user2 = CustomUser.objects.create_user(
            username='Tommy', password='Kasdf452'  # skipcq: PTC-W1006
        )

    def test_follow(self):
        """Tests to make sure str method functions with follow"""
        follow = Contact(from_user=self.user, to_user=self.user2)
        self.assertEqual("alfred follows Tommy", str(follow))
