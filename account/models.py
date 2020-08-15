"""Models for the account module"""
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import EmailField, CharField, ForeignKey, \
    DateTimeField, ManyToManyField, Model, CASCADE
from django.db.models.manager import Manager
from django.urls import reverse

from common.manager import PaginateManager
# ImageField,

class CustomUser(AbstractUser):
    """CustomUser model describes the sites users

    Attributes:
        email(EmailField): The user's email, required
        photo(ImageField): The user's photo, optional
        photo_link(CharField): The user's photo link, optional
        objects: UserManager
        paginate: PaginateManager

    Methods:
        __str__(self): Returns the users first and last name as a string
        get_absolute_url(self): Property: Returns the URL for the user's
            profile as a string, currently non functional
        photo_url(self): Property: Returns the URL of the user's profile photo
            or returns the URL of the default no-picture

    """

    email = EmailField(blank=False)
    # photo = ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    photo_link = CharField(blank=False, max_length=2000,
                           default='/static/icons/no-picture.jpg')
    biography = CharField(blank=True, max_length=1000)

    objects = UserManager()
    paginate = PaginateManager()

    class Meta:
        """The Meta

        Attributes:
            ordering: ID
        """

        ordering = ['-id']

    def __str__(self):
        """Lets a User get the first and last name as a string."""
        if self.first_name:
            if self.last_name:
                return f'{self.first_name} {self.last_name}'
            return self.first_name

        if self.last_name:
            return self.last_name
        return self.username

    @property
    def get_absolute_url(self):
        """Lets a user get the profile url, Currently non functional"""
        return {'Status': 'Coming Soon!'}
        # return reverse('user_detail', kwargs={'slug': self.username})

    @property
    def photo_url(self):
        """Lets a user get the photo URL or the default no picture URL"""
        return self.photo_link


class Contact(Model):
    """Contact model describes the relationship between users

    Attributes:
        from_user(ForeignKey): The user who started following
        to_user(ForeignKey): The user who is being followed
        created(DateTimeField): The date and time the contact was made
        objects: Manager()
        paginate: PaginateManager()
    """

    from_user = ForeignKey(CustomUser, related_name='from_user',
                           on_delete=CASCADE)
    to_user = ForeignKey(CustomUser, related_name='to_user',
                         on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True, db_index=True)

    objects = Manager()
    paginate = PaginateManager()

    class Meta:
        """The Meta

        Attributes:
            ordering: created
        """

        ordering = ('-created',)

    def __str__(self):
        """Lets a User get the 'from user follows to user' as a string"""
        return f'{self.from_user} follows {self.to_user}'


# Add following fields to User dynamically
CustomUser.add_to_class('following',
                        ManyToManyField('self', through=Contact,
                                        related_name='followers',
                                        symmetrical=False))
