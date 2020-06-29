from django.db import models


class PaginateManager(models.Manager):
    # skipcq FLK-D200
    """PaginateManager paginates results in the model for better client display.

        Attributes: None

        Methods:
            _get_followers(user, prev_set, next_set, request_type):
                Currently get a users followers list and following list.
            next_set(self, user, page_limit, prev_set, request_type):
                Obtains the next set of data from a model.
            def previous_set(self, user, page_limit, prev_set, request_type):
                Obtains the previous set of data from a model.
            def first_set(self, user, page_limit, prev_set, request_type):
                Obtains the first set of data from a model.
            def last_set(self, user, page_limit, total_followers, prev_set,
                request_type):
                Obtains the last set of data in a model.
    """

    @staticmethod
    def _get_followers(user, prev_set: int, next_set: int, request_type: str):
        """Currently get a users followers list and following list.

            Arguments:
                user (CustomUser): The user making the request
                prev_set (int): The starting index for the previous set of data
                next_set (int): The starting index for the next set of data
                request_type (str):
                    the type of request, either followers or following

            Returns: A list of either followers or people the user is following
        """
        # cannot be negative
        if prev_set < 0:
            prev_set = 0
        if request_type == 'followers':
            list = user.followers.order_by("-date_joined")[
                        prev_set:next_set]
        elif request_type == 'following':
            list = user.following.order_by("-date_joined")[
                        prev_set:next_set]
        result = []
        for people in list:
            result.append({
                'photo': people.photo_url,
                'url': people.get_absolute_url,
                'name': str(people),
                })
        return result

    def next_set(
            self, user, page_limit: int, prev_set: int, request_type: str):
        """Grabs the next set of data from a model.

            Arguments:
                user (CustomUser): The user whop is making the request
                page_limit (int): The max number of objects per request
                prev_set (int): The starting index for the previous set of data
                request_type (str): the data being requested

            Returns: a list of the data requested
        """
        next_set = prev_set + page_limit
        return self._get_followers(user, prev_set, next_set, request_type)

    def previous_set(
            self, user, page_limit: int, prev_set: int, request_type: str):
        """Grabs the previous set of data from a model.

        Arguments:
                user (CustomUser): The user whop is making the request
                page_limit (int): The max number of objects per request
                prev_set (int): The starting index for the previous set of data
                request_type (str): the data being requested

            Returns: a list of the data requested
        """
        # Going back a page, so we need to back past this page
        # and go to the begining of the previous page.
        next_set = prev_set - page_limit
        return self._get_followers(user, next_set, prev_set, request_type)

    def first_set(
            self, user, page_limit: int, prev_set: int, request_type: str):
        """Grabs the first set of data from a model.

        Arguments:
                user (CustomUser): The user whop is making the request
                page_limit (int): The max number of objects per request
                prev_set (int): The starting index for the previous set of data
                request_type (str): the data being requested

            Returns: a list of the data requested
        """
        next_set = page_limit
        prev_set = 0
        return self._get_followers(user, prev_set, next_set, request_type)

    def last_set(
            self, user, page_limit: int, total_followers: int, prev_set: int,
            request_type: str):
        """Grabs the last set of data from a model.

        Arguments:
                user (CustomUser): The user whop is making the request
                page_limit (int): The max number of objects per request
                prev_set (int): The starting index for the previous set of data
                request_type (str): the data being requested

            Returns: a list of the data requested
        """
        next_set = total_followers
        prev_set = total_followers - page_limit
        return self._get_followers(user, prev_set, next_set, request_type)
