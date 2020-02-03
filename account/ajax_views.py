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

                followers_dict = []
                for people in followers:
                    followers_dict.append({
                        'photo': people.photo_url,
                        'url': people.get_absolute_url(),
                        'name': str(people),
                        }
                    )
                return JsonResponse({
                    'status': 'OK',
                    'followers': followers_dict,
                })
            except CustomUser.DoesNotExist:
                return JsonResponse({'status': 'DoesNotExist'})
        return JsonResponse({'status': 'ko'})
