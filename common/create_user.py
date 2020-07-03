from account.models import CustomUser


default_data = {'username': 'TestUser', 'email': 'test@test.com',
                'password': 'password', 'first_name': 'first_test',
                'last_name': 'last_test'}


def create_user(user_data=default_data):
    """create_user creates a new user in the test DB.

        Parameters:
            user_data(dict): dictionary of the user data
                username: the test username
                email: the test email
                password: the test password
                first_name: the test first_name
                last_name: the test last_name
    """
    # Create a user
    user = CustomUser.objects.create(
        username=user_data['username'],
        email=user_data['email'],
        first_name=user_data['first_name'],
        last_name=user_data['last_name']
    )
    user.set_password(user_data['password'])
    user.save()
