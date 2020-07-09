from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import (CreateView, DetailView, ListView,
                                  FormView)
from django.views.generic.detail import SingleObjectMixin

from .models import Post, Comment
from .forms import PostCreateForm, CommentForm


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/create_post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.authors = self.request.user
        post.save()
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_list')


class PostListView(ListView):
    context_object_name = 'all_posts'
    model = Post
    paginate_by = 25
    template_name = 'post/post_list.html'


class PostDisplayView(DetailView):
    """View to display the post. Currently not called directly."""
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['form'] = CommentForm()
        return context


class CommentFormView(SingleObjectMixin, FormView):
    """View to display comment form. Currently not called directly."""
    model = Post
    form_class = CommentForm
    template_name = 'post/post_detail.html'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()  # skipcq PYL-W0201
        post = get_object_or_404(Post, pk=self.object.pk)
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent = post
            comment.user = request.user
            comment.save()

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDetailView(View):
    """View to shjow a Post's details including a comment form to
    logged in users."""
    @staticmethod
    def get(request, *args, **kwargs):
        view = PostDisplayView.as_view()
        return view(request, *args, **kwargs)

    @staticmethod
    def post(request, *args, **kwargs):
        view = CommentFormView.as_view()
        return view(request, *args, **kwargs)
