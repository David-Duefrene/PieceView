from django.conf import settings
from django.db import models
from django.urls import reverse

from bleach.sanitizer import Cleaner

from account.models import CustomUser


class Post(models.Model):
    """Model representing users posts.

        Attributes:
            authors(ForeignKey: CustomUser): The authors of the post
            content(TextField): The content of the post
            title(CharField): The post title
            created(DateTimeField): The time the post was created
            owner(ForeignKey: CustomUser): The owner of the post

        Methods:
            __str__: returns the title
            save: Cleans the content and sets the owner
    """
    authors = models.ForeignKey(CustomUser, null=True,
                                on_delete=models.SET_NULL,
                                related_name='author')
    content = models.TextField(blank=False)
    title = models.CharField(blank=False, max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    owner = models.ForeignKey(CustomUser, null=True,
                              on_delete=models.SET_NULL,
                              related_name='owner')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-created', 'authors',  'title')

    def __str__(self):
        return self.title

    # skipcq: PYL-W0221
    def save(self, *args, **kwargs):
        """Cleans the content with bleach and sets the owner to the author"""
        cleaner = Cleaner(tags=settings.APPROVED_TAGS,
                          attributes=settings.APPROVED_ATTRIBUTES)
        self.content = cleaner.clean(self.content)
        self.owner = self.authors
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('postRUD', kwargs={'pk': self.pk})


class Comment(models.Model):
    """Model for user comments on posts."""
    parent = models.ForeignKey(Post, on_delete=models.CASCADE,
                               related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name='users')

    body = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['created']

    def __str__(self):
        return f'Comment by {self.user} on {self.created}'
