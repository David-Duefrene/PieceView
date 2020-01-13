from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    pass


class UserRegistrationForm(forms.ModelForm):
    """
    Form fora new user to register on the site.
    required fields are username, email, and first name
    """
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'email', 'last_name', 'photo')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True

    def clean_password2(self):
        """ensures both passwords match"""
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.',
                                        code='mismatch_pass')
        return cd['password2']

    def save(self, commit=True):
        """saves the form to the database"""
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):
    """
    Form for a user to edit thier account.
    required fields are username, email, and first name just as
    UserRegistrationForm
    """
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'photo')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
