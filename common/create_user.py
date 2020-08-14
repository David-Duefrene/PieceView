"""Allows the ability to create a user for testing purposes."""
from faker import Faker

from account.models import CustomUser


def create_user(test='Fine'):
    """
    create_user creates a new user in the test DB.

            Parameters:
                user_data(dict): dictionary of the user data
                    username: the test username
                    email: the test email
                    password: the test password
                    first_name: the test first_name
                    last_name: the test last_name
    """
    generator = Faker()
    full_name = generator.name()
    full_name = full_name.split()
    username = full_name[0][0] + full_name[1] + str(generator.random)

    user = CustomUser.objects.create(
        username=username,
        email=f'{username}@test.com',
        first_name=full_name[0],
        last_name=full_name[1],
    )

    user.set_password('password')
    user.save()

    return user
