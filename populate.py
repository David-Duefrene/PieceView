import os
import django
import sys
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PieceView.settings')
django.setup()

from account.models import CustomUser


class Populate(object):
    """ Populate class describes various command to populate stuff. """

    def __init__(self):
        self.generator = Faker()
        self.password = 'asdVE5asd'

        self.command_list = {'users': self.users, 'followers': self.followers,
                             'commands': self.commands}

    def commands(self, args):
        print(self.command_list)

    def users(self, args):
        """
        Generates users. Needs 1 optional argument, number of  users to
        generate. Default is 5.
        populate users <int:num of users>
        """
        number = 5
        if args[0].isnumeric():
            number = int(args[0])

        for num in range(number):
            full_name = self.generator.name()
            full_name = full_name.split()
            username = full_name[0][0] + full_name[1]
            try:
                new_user = CustomUser.objects.get_or_create(
                    username=username,
                    email=username + '@mail.com',
                    first_name=full_name[0],
                    last_name=full_name[1],
                    password=self.password,
                    )
            except Exception:
                print("Duplicate name detected.")
                continue

    def followers(self, args):
        """
        Adds followers to DB. Need 2 arguments, first number of followers to
        generate and the second is the your username. Default is 5.
        populate followers <int:num of followers> <str:username>
        """

        if len(args) < 2:
            print(f'Invalid args: {args}')
            print('populate followers <int:num of followers> <str:username>')
            return False

        try:
            user = CustomUser.objects.get(username=args[1])
        except Exception:
            print(f'Incorrect username: {args[1]}')
            return False

        number_of_followers = 5
        all_users = CustomUser.objects.all()
        if args[0].isnumeric():
            number_of_followers = int(args[0])

        counter = 0
        for users in all_users:
            if user == users:
                continue

            if counter >= number_of_followers:
                print('I have finished adding followers')
                break

            if users in user.followers.all():
                continue

            follow = users.following.add(user)
            # print(f'{users} follow: {user}')
            counter += 1


if __name__ == "__main__":
    Pop = Populate()
    if len(sys.argv) < 2:
        print('Type command and optional number of time to run said command.')
        print('For a list of commands Type: ')

    else:
        if sys.argv[1] in Pop.command_list:
            Pop.command_list[sys.argv[1]](sys.argv[2:])
        else:
            print(f"Invalid Command {sys.argv[1]}")
