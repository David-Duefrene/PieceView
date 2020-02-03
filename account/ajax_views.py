from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.views.decorators.http import require_POST
from django.views.generic.base import View
from django.http import HttpResponseBadRequest
from .models import CustomUser, Contact
from common.mixins import AuthAjaxOnlyMixin
from common.decorators import ajax_required


class GetFollowers(AuthAjaxOnlyMixin, View):
    """
    Retrieves the current logged on users followers. Redirects unauthenticated
    users to login. Presently offers to paginate the data. Request needs logged
    on user's ID, the number of objects per page, and the page number the
    requester wants.
    """
    @ajax_required
    def post(self, request, *arg):
        user_id = request.POST.get('id')
        page_limit = int(request.POST.get('page_limit'))
        page_num = int(request.POST.get('page_num'))
        print(f'user_id: {user_id}')
        print(f'page_limit: {page_limit}')
        print(f'page_num: {page_num}')
        if user_id and page_num:
            try:
                user = CustomUser.objects.get(id=user_id)
                total_followers = user.followers.count()
                previous_followers = page_limit * (page_num - 1)
                followers = user.followers.order_by("-date_joined")[
                    previous_followers:previous_followers+page_limit]
                print(followers)
            except CustomUser.DoesNotExist:
                return JsonResponse({'status': 'DoesNotExist'})
        return JsonResponse({'status': 'ko'})
