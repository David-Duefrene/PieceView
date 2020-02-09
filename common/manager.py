from django.db import models
from django.http import JsonResponse


class PaginateManager(models.Manager):
    """PaginateManager paginates results in the model for better client
    display."""

    def get_queryset(self):
        return super(PaginateManager,
                     self).get_queryset().filter(is_active=True)

    def paginate(self, action, user, page_limit: int, page_num: int):

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

        elif action == 'next':
            next_set = prev_set + page_limit
            page_num += 1

        elif action == 'first':
            next_set = page_limit
            prev_set = 0
            page_num = 1

        elif action == 'last':
            next_set = total_followers
            prev_set = total_followers - page_limit
            page_num = total_followers // page_limit

        else:
            print('Bad action in paginate')
            return JsonResponse({'status': 'Bad Action: 404'})

        followers = followers = user.followers.order_by("-date_joined")[
                    prev_set:next_set]

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
