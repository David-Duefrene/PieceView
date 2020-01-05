from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST

from common.decorators import ajax_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm
from .models import CustomUser, Contact

def user_login(request):
	if request.user.is_authenticated:
		return render(request, 'user/dashboard.html', {'section': 'dashboard'})
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'],
								  password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return render(request, 'user/dashboard.html', {'section': 'dashboard'})
				else:
					return HttpResponse('Disabled account')
			else:
				return render(request, 'registration/login_invalid.html', {'form': form})
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
			return render(request, 'registration/register_done.html',
							{'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'registration/register.html',
				  {'user_form': user_form})

@login_required
def dashboard(request):
	return render(request, 'user/dashboard.html', {'section': 'dashboard'})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
		if user_form.is_valid():
			user_form.save()
	else:
		user_form = UserEditForm(instance=request.user)
	return render(request, 'user/edit.html',
					{'user_form': user_form})

@login_required
def user_list(request):
    users = CustomUser.objects.filter(is_active=True)
    return render(request, 'user/people.html', {'users': users})

@login_required
def user_detail(request, username):
    user = get_object_or_404(CustomUser, username=username, is_active=True)
    return render(request, 'user/profile.html',
                  {'section': 'profile', 'user': user})

@ajax_required
@require_POST
@login_required
def user_follow(request):
	user_id = request.POST.get('id')
	action = request.POST.get('action')
	if user_id and action:
		try:
			user = CustomUser.objects.get(id=user_id)
			if action == 'follow':
				Contact.objects.get_or_create(from_user=request.user, to_user=user)
			else:
				Contact.objects.filter(from_user=request.user, to_user=user).delete()
			return JsonResponse({'status':'ok'})

		except CustomUser.DoesNotExist:
			return JsonResponse({'status':'ko'})

	return JsonResponse({'status':'ko'})
