# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm

# from django import forms


# class UserRegistrationForm(UserCreationForm):
#     """
#     Form for a new user to register on the site.
#     Required fields are username, email, and passwords.
#     """
#     password1 = forms.CharField(label='Password',
#                                 widget=forms.PasswordInput(
#                                     attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label='Repeat password',
#                                 widget=forms.PasswordInput(
#                                     attrs={'class': 'form-control'}))

#     class Meta:
#         model = get_user_model()
#         fields = ('username', 'email', 'first_name', 'last_name') #, 'photo')

#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             # 'photo': forms.FileInput(
#             #     attrs={'class': 'form-control custom-file-input'}),
#         }


# class UserEditForm(forms.ModelForm):
#     """
#     Form for a user to edit thier account.
#     Required fields is just email. Does not
#     inherit from UserChangeForm to avoid setting
#     a password in this form.
#     """
#     class Meta:
#         model = get_user_model()
#         fields = ('first_name', 'last_name', 'email' # 'photo', )

#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             # 'photo': forms.FileInput(
#             #     attrs={'class': 'form-control custom-file-input'}),
#         }
