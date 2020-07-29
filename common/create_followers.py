from account.models import Contact

from common.create_user import create_user

default_contacts = [{'username': 'TestUser1', 'email': 'test1@test.com',
                    'password': 'password', 'first_name': 'first_test1',
                     'last_name': 'last_test1'},
                    {'username': 'TestUser2', 'email': 'test2@test.com',
                    'password': 'password', 'first_name': 'first_test2',
                     'last_name': 'last_test2'},
                    {'username': 'TestUser3', 'email': 'test3@test.com',
                    'password': 'password', 'first_name': 'first_test3',
                     'last_name': 'last_test3'}
                    ]


def create_followers(contacts=default_contacts):
    user = create_user()
    for each in contacts:
        follower = create_user(each)
        Contact.objects.create(from_user=follower, to_user=user)


def create_following(contacts=default_contacts):
    user = create_user()
    for each in contacts:
        to_follow = create_user(each)
        Contact.objects.create(from_user=user, to_user=to_follow)
