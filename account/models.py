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

class Contact(models.Model):
    """
    Contact model describes the relationship between users
    """
    from_user = models.ForeignKey(CustomUser, related_name='from_user',
                                  on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='to_user',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.from_user} follows {self.to_user}'

# Add following field to User dynamically
CustomUser.add_to_class('contacts', models.ManyToManyField('self', through=Contact,
                                         related_name='followers', symmetrical=False))
