from django.conf import settings
from django.db import models
from django.urls import reverse

from bleach.sanitizer import Cleaner

from account.models import CustomUser


class Post(models.Model):
    """ Model representing users posts."""
    authors = models.ForeignKey(CustomUser, null=True,
                                on_delete=models.SET_NULL)
    content = models.TextField(blank=False)
    title = models.CharField(blank=False, max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-created', 'authors',  'title')

    def __str__(self):
        return self.title

    # skipcq: PYL-W0221
    def save(self, *args, **kwargs):
        cleaner = Cleaner(tags=settings.APPROVED_TAGS,
                          attributes=settings.APPROVED_ATTRIBUTES)
        self.content = cleaner.clean(self.content)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    """ Model for user comments on posts."""
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
        return f'Comment by {self.comentor} on {self.created}'
