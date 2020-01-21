from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Post
from .forms import PostCreateForm


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/create_post.html'

    def form_valid(self, form):
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('create_post')
