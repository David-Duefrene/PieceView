from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView, ListView, DetailView,\
                                    TemplateView

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


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    """View for a users dashboard"""
    template_name = 'user/dashboard.html'


class EditProfileView(UpdateView):
    """View for allowing a user to edit thier profile"""
    model = CustomUser
    form_class = UserEditForm
    template_name = 'user/edit.html'

    def user_passes_test(self, request):
        """test to see if the profile belongs to the user"""
        # Deepsource wants object declared in __init__, which Django does not
        # recomend overriding in a view class, ignoring the warning.
        # skipcq: PYL-W0201
        self.object = self.get_object()
        return self.object == request.user

    def dispatch(self, request, *args, **kwargs):
        """
        Overrides default dispatch to force a non-authenticated user to login
        and to ensure a user who tries to edit a different user's profile gets
        redirected to their own dashboard.
        """
        if request.user.is_authenticated:
            if not self.user_passes_test(request):
                return render(request, 'user/dashboard.html')
            return super(EditProfileView, self).dispatch(
                request, *args, **kwargs)
        return redirect_to_login(request.get_full_path())


class UserListView(LoginRequiredMixin, ListView):
    """View displaying all users"""
    model = CustomUser
    paginate_by = 25
    template_name = 'user/people.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    """view displaying a users profile"""
    context_object_name = 'profile'
    model = CustomUser
    slug_field = 'username'
    template_name = 'user/profile.html'


@ajax_required
@require_POST
@login_required
def user_follow(request):
    """
    View for a user following another user.  Only permited via ajax + POST via
    a authenticated user.
    """
    user_id = request.POST.get('id')
    action = request.POST.get('action')

    if user_id and action:
        try:
            user = CustomUser.objects.get(id=user_id)

            if action == 'follow':
                Contact.objects.get_or_create(from_user=request.user,
                                              to_user=user)
                return JsonResponse({'status': 'follow'})
            Contact.objects.filter(from_user=request.user,
                                   to_user=user).delete()
            return JsonResponse({'status': 'unfollow'})

        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'DoesNotExist'})

    return JsonResponse({'status': 'ko'})
