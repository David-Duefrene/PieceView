"""
### urls.py
### urls config for the account application
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Default authentication URL
    path('', include('django.contrib.auth.urls')),
    # Registration URL
    path('register/', views.register, name='register'),
]
