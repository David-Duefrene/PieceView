from account.models import Contact

from common.create_user import create_user


def create_followers():
    user = create_user()
    followers = []
    for each in range(3):
        follower = create_user()
        followers.append(follower.username)
        Contact.objects.create(from_user=follower, to_user=user)
    return {'contacts': followers, 'user': user}


def create_following():
    user = create_user()
    following = []
    for each in range(3):
        to_follow = create_user()
        following.append(to_follow.username)
        Contact.objects.create(from_user=user, to_user=to_follow)
    return {'contacts': following, 'user': user}
