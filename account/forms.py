"""
### forms.py
### form classes for the account application
### Copyright 2019 David J Duefrene, All rights reserved.
"""
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserManager(BaseUserManager):
    pass

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        # email = {'required': True}
        model = get_user_model()
        fields = ('username', 'first_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    def clean_password2(self):
        """
        ensures both passwords match
        """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        """
        saves the form to the database
        """
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
