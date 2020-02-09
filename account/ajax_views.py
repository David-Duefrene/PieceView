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
            action = request.POST.get('action')
            user = request.user
            return CustomUser.paginate.paginate(action, user,
                                                page_limit, page_num)
        except Exception as e:
            print('bad data GetFollowers')
            print(f'{e}')
            return JsonResponse({'status': 'Bad Data: 404'})
