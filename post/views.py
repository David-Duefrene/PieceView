from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Post
from .forms import PostCreateForm


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


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_field = 'pk'
    template_name = 'post/post_detail.html'


class PostListView(ListView):
    context_object_name = 'all_posts'
    model = Post
    paginate_by = 25
    template_name = 'post/post_list.html'
