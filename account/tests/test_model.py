from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

import os

from account.models import CustomUser


class CustomUserModelTest(TestCase):
    """Tests are customer user model"""
    def test_default_photo_url(self):
        """tests the photo url"""
        test_user = CustomUser()
        self.assertEqual("/static/icons/no-picture.jpg", test_user.photo_url)

    def test_custom_photo_url(self):
        """tests correct url if a user uploads there own photo"""
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  'alber-einstien.jpg')
        test_user = CustomUser()
        test_user.photo = SimpleUploadedFile(name='test_image.jpg',
                                             content=open(image_path,
                                                          'rb').read(),
                                             content_type='image/jpeg')
        self.assertEqual("/media/test_image.jpg", test_user.photo_url)
