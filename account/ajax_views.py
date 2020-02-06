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
        page_limit = int(request.POST.get('page_limit'))
        page_num = int(request.POST.get('page_num'))
        action = request.POST.get('action')

        try:
            user = request.user
            total_followers = user.followers.count()
            prev_set = page_limit * (page_num)

            # both statements keep us in bounds
            if prev_set < page_limit:
                action = 'first'
            if prev_set >= total_followers:
                action = 'last'

            if action == 'previous':
                # Going back a page, so we need to back past this page
                # and go to the begining of the previous page.
                next_set = prev_set - page_limit * 2
                page_num -= 1
                followers = user.followers.order_by("-date_joined")[
                    next_set:prev_set]

            # user hit next set of cards
            elif action == 'next':
                next_set = prev_set + page_limit
                page_num += 1
                followers = user.followers.order_by("-date_joined")[
                    prev_set:next_set]

            # user wants 1st set of cards
            elif action == 'first':
                next_set = page_limit
                prev_set = 0
                page_num = 1
                followers = user.followers.order_by("-date_joined")[
                    prev_set:next_set]

            # and user wants last set
            elif action == 'last':
                next_set = total_followers
                prev_set = total_followers - page_limit
                page_num = total_followers // page_limit
                followers = user.followers.order_by("-date_joined")[
                    prev_set:next_set]

            else:  # something has gone haywire if we are here.
                return JsonResponse({'status': 'ko'})

            # create the dict of followers for the front end.
            followers_dict = []
            for people in followers:
                followers_dict.append({
                    'photo': people.photo_url,
                    'url': people.get_absolute_url(),
                    'name': str(people),
                    })

            # finally return the data.
            return JsonResponse({
                'status': 'OK',
                'followers': followers_dict,
                'new_page': page_num,
            })
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'DoesNotExist'})
        return JsonResponse({'status': 'ko'})
