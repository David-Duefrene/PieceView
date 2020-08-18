"""URLs list for the account module."""
from django.urls import path, include

from rest_framework import routers

from knox import views as knox_views

from .api import LoginAPI, ContactsAPI, UserAPI, UserEdit

router = routers.DefaultRouter()

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/account', UserAPI.as_view({'post': 'create', 'get': 'list'}),
         name='api_account'),
    path('api/account/edit/<pk>', UserEdit.as_view(), name='edit_account'),
    path('api/auth/login', LoginAPI.as_view(), name='log_API'),
    path('api/contacts', ContactsAPI.as_view({'get': 'list'}),
         name='contacts_API'),
    path('api/auth/logout', knox_views.LogoutView.as_view(),
         name='logout_API'),
] + router.urls
