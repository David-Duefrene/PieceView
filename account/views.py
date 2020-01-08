from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView, UpdateView

from common.decorators import ajax_required
from .forms import UserRegistrationForm, UserEditForm
from .models import CustomUser, Contact


class UserRegisterCreateView(CreateView):
    """User registration View. Overrides form_valid to render a template"""
    model = CustomUser
    form_class = UserRegistrationForm
    success_url = 'registration/register_done.html'
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'registration/register_done.html',
                      self.get_context_data())


@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html', {'section': 'dashboard'})


class EditProfileView(UpdateView):
    model = CustomUser
    form_class = UserEditForm
    template_name = 'user/edit.html'


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
                Contact.objects.get_or_create(from_user=request.user,
                                              to_user=user)
            else:
                Contact.objects.filter(from_user=request.user,
                                       to_user=user).delete()
            return JsonResponse({'status': 'ok'})

        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'ko'})

    return JsonResponse({'status': 'ko'})
