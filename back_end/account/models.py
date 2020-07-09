from django.db import models
from django.db.models.manager import Manager
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

from common.manager import PaginateManager


class CustomUser(AbstractUser):
    """CustomUser model describes our sites users."""
    email = models.EmailField(blank=False)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    objects = UserManager()
    paginate = PaginateManager()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        if self.first_name:
            if self.last_name:
                return f'{self.first_name} {self.last_name}'
            return self.first_name

        if self.last_name:
            return self.last_name
        return self.username

    @property
    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'slug': self.username})

    @property
    def photo_url(self):
        """Returns the users photo url or the default no picture url."""
        if self.photo:
            return self.photo.url
        return "/static/icons/no-picture.jpg"


class Contact(models.Model):
    """Contact model describes the relationship between users."""
    from_user = models.ForeignKey(CustomUser, related_name='from_user',
                                  on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='to_user',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    objects = Manager()
    paginate = PaginateManager()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.from_user} follows {self.to_user}'


# Add following fields to User dynamically
CustomUser.add_to_class('following',
                        models.ManyToManyField('self',
                                               through=Contact,
                                               related_name='followers',
                                               symmetrical=False))
