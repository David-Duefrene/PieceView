"""
### admin.py
### admin functions for account application
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistrationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	add_form = UserRegistrationForm
	model = CustomUser
	list_display = ['username', 'email', 'is_staff',]
	fieldsets = (
		(None, {'fields': ('username', 'email', 'password', 'first_name')}),
		('Permissions', {'fields': ('is_staff', 'is_active')}),
	)
	add_fieldsets = (
		(None, {'classes': ('wide',),
			'fields': ('username', 'email', 'password', 'password2', 'is_staff', 'is_active')}),
	)
	search_fields = ('email', 'username',)
	ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
