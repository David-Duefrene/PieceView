from django import forms

from .models import Post


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
