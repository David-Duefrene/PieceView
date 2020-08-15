# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from .forms import UserRegistrationForm
# from .models import CustomUser, Contact


# class CustomUserAdmin(UserAdmin):
#     add_form = UserRegistrationForm
#     model = CustomUser
#     list_display = ['username', 'email', 'is_staff']

#     # To edit a existing user
#     fieldsets = ((None, {'fields': ('username', 'email', 'password',
#                   'first_name', 'last_name', 'photo')}),
#                  ('Permissions', {'fields': ('is_staff', 'is_active')}))
#     # To add a new user
#     add_fieldsets = ((None, {'classes': ('wide',),
#                      'fields': ('username', 'email', 'password', 'password2',
#                                 'first_name', 'is_staff', 'is_active',
#                                 'last_name', 'photo')}))

#     search_fields = ('email', 'username', 'first_name', 'last_name')
#     ordering = ('username',)


# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Contact)
