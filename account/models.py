from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    """CustomerUser model describes our sites users"""
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        """Returns the user detail page"""
        return reverse('user_detail', kwargs={'username': self.username})

    @property
    def photo_url(self):
        """Returns the users phot url or the default no pucture url"""
        if self.photo:
            return self.photo.url
        return "/static/icons/no-picture.jpg"


class Contact(models.Model):
    """Contact model describes the relationship between users"""
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
CustomUser.add_to_class('contacts', models.ManyToManyField('self',
                        through=Contact, related_name='followers',
                        symmetrical=False))
