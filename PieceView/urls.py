"""
### urls.py
### master url mappings for the PieceView project
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
	path('admin/', admin.site.urls),
	path('account/', include('account.urls')),
]
