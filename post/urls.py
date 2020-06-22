from django.urls import path

from . import views
from .api import PostAPI

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('list/', views.PostListView.as_view(), name='post_list'),
    path('<pk>/', views.PostDetailView.as_view(), name='post_detail'),


    # Paths for API calls
    path('api/postList', PostAPI.as_view({'get': 'list'}), name='post_API'),
]
