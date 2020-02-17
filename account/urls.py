from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . import ajax_views

urlpatterns = [
    path('', views.DashboardTemplateView.as_view(), name='dashboard'),

    # previous login/logout views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # Registration URL
    path('register/', views.UserRegisterCreateView.as_view(), name='register'),

    # URLs for various contacts
    path('users/follow/', views.user_follow, name='user_follow'),

    # Edit Profile
    path('edit/<pk>/', views.EditProfileView.as_view(), name='edit'),
    path('people/', views.UserListView.as_view(), name='user_list'),
    path('people/<slug>/', views.UserDetailView.as_view(), name='user_detail'),

    # Ajax requests
    path('ajax/users', ajax_views.GetUsers.as_view(), name='get_users'),
]
