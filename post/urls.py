from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('list/', views.PostListView.as_view(), name='post_list'),
    path('<pk>/', views.PostDetailView.as_view(), name='post_detail'),

]
