from django.http import JsonResponse

from .models import CustomUser
from common.mixins import AuthAjaxOnlyMixin


class GetFollowers(AuthAjaxOnlyMixin):
    """
    Retrieves the current logged on user’s followers. Redirects
    unauthenticated users to login. Presently offers to paginate the data.
    Request needs logged on user's ID, the number of objects per page, and the
    page number the requester wants.
    """

    def post(self, request, *arg):
        user_id = request.POST.get('id')
        page_limit = int(request.POST.get('page_limit'))
        page_num = int(request.POST.get('page_num'))
        action = request.POST.get('action')

        try:
            user = request.user
            total_followers = user.followers.count()
            prev_set = page_limit * (page_num - 1)

            if action == 'next':
                next_set = prev_set + page_limit
                page_num += 1
            elif action == 'previous':
                next_set = prev_set + page_limit
                page_num -= 1
            elif action == 'first':
                next_set = page_limit
                prev_set = 0
                page_num = 0
            elif action == 'last':
                next_set = total_followers
                prev_set = total_followers - page_limit
                page_num = total_followers // page_limit
            else:
                return JsonResponse({'status': 'ko'})

            followers = user.followers.order_by("-date_joined")[
                prev_set:next_set]

            followers_dict = []
            for people in followers:
                followers_dict.append({
                    'photo': people.photo_url,
                    'url': people.get_absolute_url(),
                    'name': str(people),
                    })

            return JsonResponse({
                'status': 'OK',
                'followers': followers_dict,
                'new_page': page_num,
            })
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'DoesNotExist'})
        return JsonResponse({'status': 'ko'})
