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
        try:
            page_limit = int(request.POST.get('page_limit'))
            page_num = int(request.POST.get('page_num'))
            user = request.user
            total_followers = user.followers.count()
            prev_set = page_limit * (page_num)
            followers = []
            action = request.POST.get('action')

            # Both statements keep us in bounds
            if prev_set < page_limit:
                action = 'first'
            if prev_set > total_followers:
                action = 'last'

            if action == 'next':
                followers = CustomUser.paginate.next_set(
                    user, page_limit, total_followers, prev_set)
                page_num += 1
            elif action == 'previous':
                followers = CustomUser.paginate.previous_set(
                    user, page_limit, total_followers, prev_set)
                page_num -= 1
            elif action == 'first':
                followers = CustomUser.paginate.first_set(
                    user, page_limit, total_followers, prev_set)
                page_num = 1
            elif action == 'last':
                followers = CustomUser.paginate.last_set(
                    user, page_limit, total_followers, prev_set)
                page_num = total_followers // page_limit

            if followers:
                print(f'page number: {page_num}')
                return JsonResponse({
                    'status': 'OK',
                    'followers': followers,
                    'new_page': page_num,
                })

            return JsonResponse({'status': 'Bad Request: Bad Action.'})
        except Exception as e:
            print('bad data GetFollowers')
            print(f'{e}')
            return JsonResponse({'status': 'Bad Data: 404'})
