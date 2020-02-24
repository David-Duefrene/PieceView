from django.http import JsonResponse

from .models import CustomUser

from common.mixins import AuthAjaxOnlyMixin



class GetUsers(AuthAjaxOnlyMixin):
    """
    Retrieves the current logged on user’s followers. Redirects
    unauthenticated users to login. Presently offers to paginate the data.
    Request needs logged on user's ID, the number of objects per page, and the
    page number the requester wants.
    """

    @staticmethod
    def post(request):
        try:
            page_limit = int(request.POST.get('page_limit'))
            page_num = int(request.POST.get('page_num'))
            user = request.user
            prev_set = page_limit * (page_num)
            request_type = request.POST.get('request_type')
            action = request.POST.get('action')

            if request_type == 'followers':
                total_followers = user.followers.count()
            elif request_type == 'following':
                total_followers = user.following.count()
            else:
                return JsonResponse({'status': 'Bad request_type',
                                     'rejected_type': request_type})

            # Both statements keep us in bounds
            if prev_set < page_limit:
                action = 'first'
            if prev_set > total_followers:
                action = 'last'

            if action == 'next':
                followers = CustomUser.paginate.next_set(
                    user, page_limit, prev_set, request_type)
                page_num += 1
            elif action == 'previous':
                followers = CustomUser.paginate.previous_set(
                    user, page_limit, prev_set, request_type)
                page_num -= 1
                if page_num < 1:
                    page_num = 1
            elif action == 'first':
                followers = CustomUser.paginate.first_set(
                    user, page_limit, prev_set, request_type)
                page_num = 1
            elif action == 'last':
                followers = CustomUser.paginate.last_set(
                    user, page_limit, total_followers, prev_set, request_type)
                page_num = total_followers // page_limit

            if followers:
                return JsonResponse({
                    'status': 'OK',
                    request_type: followers,
                    'new_page': page_num,
                })

            return JsonResponse({'status': 'Bad Request: Bad Action.'})
        # skipcq: PYL-W0703
        except Exception as e:
            print(f'Exeption in GetUsers.post: {e}')
            return JsonResponse({'status': 'Bad Data: 404', 'exception': e})
