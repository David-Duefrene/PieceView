from django import forms

from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    """ Form for a user to create a post """

    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """saves the form to the database"""
        new_post = super().save(commit=True)
        return new_post


class CommentForm(forms.ModelForm):
    """ Form for a user to create a comment attached to a post."""

    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        return cleaned_data
