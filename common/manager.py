from django.db import models
from django.http import JsonResponse


class PaginateManager(models.Manager):
    """ PaginateManager paginates results in the model for better client
    display."""

    def _get_followers(self, user, prev_set: int, next_set: int):
        # cannot be negitive
        if prev_set < 0:
            prev_set = 0

        followers = user.followers.order_by("-date_joined")[
                    prev_set:next_set]
        followers_dict = []
        for people in followers:
            followers_dict.append({
                'photo': people.photo_url,
                'url': people.get_absolute_url(),
                'name': str(people),
                })
        return followers_dict

    def get_queryset(self):
        """ Returns all active user accounts."""
        return super(PaginateManager,
                     self).get_queryset().filter(is_active=True)

    def next_set(
        self, user,
        page_limit: int,
        total_followers: int, prev_set: int
            ):
        """ Grabs the next set of data."""
        next_set = prev_set + page_limit
        return self._get_followers(user, prev_set, next_set)

    def previous_set(self, user, page_limit: int,
                     total_followers: int, prev_set: int, page_num):
        """ Grabs the previous set of data."""
        # Going back a page, so we need to back past this page
        # and go to the begining of the previous page.
        next_set = prev_set - page_limit * 2
        return self._get_followers(user, prev_set, next_set)

    def first_set(self, user, page_limit: int,
                  total_followers: int, prev_set: int):
        """ Grabs the first set of data."""
        next_set = page_limit
        prev_set = 0
        return self._get_followers(user, prev_set, next_set)

    def last_set(self, user, page_limit: int,
                 total_followers: int, prev_set: int):
        """ Grabs the last set of data."""
        next_set = total_followers
        prev_set = total_followers - page_limit
        return self._get_followers(user, prev_set, next_set)
