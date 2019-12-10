"""
### models.py
### model classes for the account application
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
