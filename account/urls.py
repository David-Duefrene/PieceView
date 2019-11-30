# URLs config for the account aplication
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  # Authentication URL
  path('', include('django.contrib.auth.urls')),
  # Registration URL
  path('register/', views.register, name='register'),
]
