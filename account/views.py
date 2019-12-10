from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import LoginForm, UserRegistrationForm

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request,
								 username=cd['username'],
								  password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated '\
										'successfully')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid Login')
	else:
		form = LoginForm()
	return render(request, 'registration/login.html', {'form': form})

def register(request):
  if request.method == 'POST':
	  user_form = UserRegistrationForm(request.POST)
	  if user_form.is_valid():
	  # Create a new user object but don't save it
		  new_user = user_form.save(commit=False)
	  # Set the chosen password
		  new_user.set_password(user_form.cleaned_data['password'])
	  # Save the user
		  new_user.save()
		  return render(request, 'account/register_done.html',
					{'new_user': new_user})
  else:
	  user_form = UserRegistrationForm()
  return render(request, 'account/register.html',
				  {'user_form': user_form})

@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html',
				  {'section': 'dashboard'})
