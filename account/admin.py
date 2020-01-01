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
	fieldsets = ( # To edit a existing user
		(None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'photo' )}),
		('Permissions', {'fields': ('is_staff', 'is_active')}),
	)
	add_fieldsets = ( # To add a new user
		(None, {'classes': ('wide',),
			'fields': ('username', 'email', 'password', 'password2', 'first_name',
						'is_staff', 'is_active', 'last_name', 'photo' )}),
	)
	search_fields = ('email', 'username', 'first_name', 'last_name')
	ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
