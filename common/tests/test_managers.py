from django.test import TestCase

from account.models import CustomUser, Contact

from populate import Populate


class PaginateManagerTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',
        )

    def test_next_set(self):
        pop = Populate()
        pop.users(['12'])
        pop.followers(['12', 'alfred'])

        followers = self.user.followers.all()
        test_list = Contact.paginate.next_set(
                    user=self.user, page_limit=5, prev_set=0,
                    request_type='followers')

        counter = 0
        for case in test_list:
            self.assertEqual(followers[counter].get_absolute_url(),
                             case['url'])
            counter += 1

        test_list = Contact.paginate.next_set(
                    user=self.user, page_limit=5, prev_set=5,
                    request_type='followers')
        for case in test_list:
            self.assertEqual(followers[counter].get_absolute_url(),
                             case['url'])
            counter += 1

    def test_previous_set(self):
        pop = Populate()
        pop.users(['15'])
        pop.followers(['15', 'alfred'])

        followers = self.user.followers.all()
        test_list = Contact.paginate.next_set(
                    user=self.user, page_limit=5,
                    prev_set=10, request_type='followers')

        test_list.reverse()
        counter = 14
        for case in test_list:
            self.assertEqual(followers[counter].get_absolute_url(),
                             case['url'])
            counter -= 1

        test_list = Contact.paginate.previous_set(
                    user=self.user, page_limit=5, prev_set=10,
                    request_type='followers')

        test_list.reverse()
        for case in test_list:
            self.assertEqual(followers[counter].get_absolute_url(),
                             case['url'])
            counter -= 1

        test_list = Contact.paginate.previous_set(
                    user=self.user, page_limit=5, prev_set=5,
                    request_type='followers')

        test_list.reverse()
        for case in test_list:
            self.assertEqual(followers[counter].get_absolute_url(),
                             case['url'])
            counter -= 1

    def test_first_set(self):
        pop = Populate()
        pop.users(['12'])
        pop.followers(['12', 'alfred'])

        followers = self.user.followers.all()
        test_list = Contact.paginate.first_set(
                    user=self.user, page_limit=5, prev_set=0,
                    request_type='followers')

        counter = 0
        for case in test_list:
            self.assertEqual(followers[counter].get_absolute_url(),
                             case['url'])
            counter += 1

    def test_last_set(self):
        pop = Populate()
        pop.users(['10'])
        pop.followers(['12', 'alfred'])

        followers = self.user.followers.all()
        test_list = Contact.paginate.first_set(
                    user=self.user, page_limit=5, prev_set=0,
                    request_type='followers')

        counter = 0
        for case in test_list:
            self.assertEqual(followers[counter].get_absolute_url(),
                             case['url'])
            counter += 1
