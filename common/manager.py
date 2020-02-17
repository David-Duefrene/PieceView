from django.db import models


class PaginateManager(models.Manager):
    """ PaginateManager paginates results in the model for better client
    display."""

    @staticmethod
    def _get_followers(user, prev_set: int, next_set: int):
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

# Removed get_query_set due to Contacts model not having an active status

    def next_set(self, user, page_limit: int, prev_set: int):
        """ Grabs the next set of data."""
        next_set = prev_set + page_limit
        return self._get_followers(user, prev_set, next_set)

    def previous_set(self, user, page_limit: int, prev_set: int):
        """ Grabs the previous set of data."""
        # Going back a page, so we need to back past this page
        # and go to the begining of the previous page.
        next_set = prev_set - page_limit
        return self._get_followers(user, next_set, prev_set)

    def first_set(self, user, page_limit: int, prev_set: int):
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
