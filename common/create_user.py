from faker import Faker

from account.models import CustomUser


# default_data = {'username': 'TestUser', 'email': 'test@test.com',
#                 'password': 'password', 'first_name': 'first_test',
#                 'last_name': 'last_test'}


def create_user():  # user_data=default_data):
    """create_user creates a new user in the test DB.

        # Parameters:
        #     user_data(dict): dictionary of the user data
        #         username: the test username
        #         email: the test email
        #         password: the test password
        #         first_name: the test first_name
        #         last_name: the test last_name
    """
    # Create a user
    generator = Faker()
    full_name = generator.name()
    full_name = full_name.split()
    # first initial of firstname + last name
    username = full_name[0][0] + full_name[1]
    user = CustomUser.objects.create(
        username=username,
        email=f'{username}@test.com',
        first_name=full_name[0],
        last_name=full_name[1],
    )
    user.set_password('password')
    user.save()
    return user
