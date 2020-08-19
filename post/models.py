"""Models for the posts and comments"""
from django.conf import settings
from django.db import models
from django.urls import reverse

from bleach.sanitizer import Cleaner

from account.models import CustomUser


class Post(models.Model):
    """Model representing users posts

    Attributes:
        authors(ForeignKey: CustomUser): The authors of the post
        content(TextField): The content of the post
        title(CharField): The post title
        created(DateTimeField): The time the post was created
        owner(ForeignKey: CustomUser): The owner of the post

    Methods:
        __str__: returns the title
        save: Cleans the content and sets the owner
        get_absolute_url: Gets the URL of the post
        summary: Returns the first 1000 char of a post
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
        """The Meta

        Attributes:
            verbose_name: Post
            verbose_name: Posts
            ordering: created authors title

        """

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-created', 'authors', 'title')

    def __str__(self):
        """Return the title"""
        return self.title

    # skipcq: PYL-W0221
    def save(self, *args, **kwargs):
        """Clean the content with bleach and set the owner to the author"""
        cleaner = Cleaner(tags=settings.APPROVED_TAGS,
                          attributes=settings.APPROVED_ATTRIBUTES)
        self.content = cleaner.clean(self.content)
        self.owner = self.authors
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return th eURL for the post"""
        return reverse('postRUD', kwargs={'pk': self.pk})

    @property
    def summary(self):
        """Return a summary to the content for post list"""
        return self.content[:1000]


class Comment(models.Model):
    """Model for user comments on posts

    Attributes:
        parent(ForeignKey: Post): The Post the user commented on
        body(TextField): The content of the comment
        created(DateTimeField): The time the comment was created
        user(ForeignKey: CustomUser): The owner of the comment

    Methods:
        __str__: returns the title
    """

    parent = models.ForeignKey(Post, on_delete=models.CASCADE,
                               related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name='users')

    body = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        """The Meta

        Attributes:
            verbose_name: Comment
            verbose_name: Comments
            ordering: created

        """

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['created']

    def __str__(self):
        """Return Comment bu user on DATA"""
        return f'Comment by {self.user} on {self.created}'
