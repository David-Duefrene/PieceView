from django.db import models
from django.urls import reverse

from account.models import CustomUser


class Post(models.Model):
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

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
