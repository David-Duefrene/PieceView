"""
### models.py
### model classes for the account application
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        else:
            return "/static/icons/no-picture.jpg"
