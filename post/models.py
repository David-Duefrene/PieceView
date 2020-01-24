from django.db import models
from django.urls import reverse

from bleach.sanitizer import Cleaner

from account.models import CustomUser

TAGS = [
    "a", "abbr", "area", "b", "bdo", "blockquote", "br", "caption", "cite",
    "code", "col", "colgroup", "dd", "del", "details", "dfn", "div", "dl",
    "dt", "em", "figcaption", "figure", "footer", "h1", "h2", "h3", "h4", "h5",
    "h6", "header", "i", "img", "ins", "li", "main", "map", "mark", "meter",
    "ol", "p", "picture", "pre", "progress", "q", "s", "samp", "section",
    "small", "span", "strong", "sub", "summary", "sup", "table", "tbody", "td",
    "tfoot", "th", "thead", "time", "tr", "u", "ul", "var",
]

ATTRIBUTES = {
    "img": ["src", "alt", "title"],
    "a": ["href", "alt", "title"],
}


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

    def save(self):
        cleaner = Cleaner(tags=TAGS, attributes=ATTRIBUTES)
        self.content = cleaner.clean(self.content)
        super().save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
