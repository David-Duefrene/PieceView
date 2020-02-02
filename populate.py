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

    def users(self, account=5):
        """ Generates users. """
        for num in range(account):
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


if __name__ == "__main__":
    Pop = Populate()
    if sys.argv[1] == 'users':
        if sys.argv[2].isnumeric():
            Pop.users(int(sys.argv[2]))
        else:
            Pop.users()
    else:
        print(f"Invalid Command {sys.argv[1]}")
