"""Allows user to access accout functions"""
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from django.contrib.auth.hashers import make_password

from knox.models import AuthToken

from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer, \
    UserEditSerializer


class UserAPI(ModelViewSet):
    """API to allow a user to create an account

    Attributes:
        PageNumberPagination.page_size(int): 5
        queryset: CustomUser.objects.all
        serializer_class: UserSerializer
        permission_classes: AllowAny

    Methods:
        create(self, request, *args, **kwargs): Creates a user
    """

    PageNumberPagination.page_size = 5
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """Will create an account

        Allows a non-authenticated user to create an account

        Request.data:
            username(string): The new users username
            password(string): The new users password
            email(string): The new users email
            first_name(string): The new users first name
            last_name(string): The new users last name

        Returns Response:
            user(object): The user itself
            token(string): The new user's authentication token
        """
        if request.data['password'] is not None:
            hashed_pass = make_password(request.data['password'])
            request.data['password'] = hashed_pass

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserEdit(RetrieveUpdateDestroyAPIView):
    """Retrieves, updates and deletes a user

    Allows anyone to view a profile but will restrict updating or deleting a
    user to the current logged on user only

    Attributes:
        queryset: Set to all Users
        serializer_class: Uses UserSerializer
        edit_serializer: UserEditSerializer
        permission_classes: Sets non-authenticated & non-owners to read only

    Methods:
        patch(self, request, *args, **kwargs): Allow an authenticated user to
        update their profile
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    edit_serializer = UserEditSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def patch(self, request, *args, **kwargs):
        """Will allows a user to update their profile

        Allows a user to change their first name, last name and email.

        Request Data: JSON(string)
            first_name: User's first name
            last_name: User's last name
            email: User's email
        """
        instance = request.user
        instance.first_name = request.data['first_name']
        instance.last_name = request.data['last_name']
        instance.email = request.data['email']
        instance.save()

        serializer = self.edit_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        return Response(serializer.data)


class LoginAPI(GenericAPIView):
    """Allows a user to login

    Allows an already registered user to login to the site.

    Attributes:
        serializer_class: LoginSerializer

    Methods:
        post(self, request, *args, **kwargs): Logs the user in.
    """

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """Will allow a user to get authentication token and user object

        Request Data:
            username(string): The user's username
            password(string): The user's password

        Returns Response:
            user(object): The user who just logged in
                username(string):
                email(string): The user's email
                photo(file): The user's photo file
                first_name(string): The user's first name
                last_name(string): The user's last name
                followers(list): The users' foolower's primary key
                    To be depreciated
                photo_url(string): The url to the user's profile photo
                get_absolute_url(string): The url to the user's profile
                    Currently non functional
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
            "user": UserSerializer(
                user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class ContactsAPI(ModelViewSet):
    """Will retrieve a user's contacts list

    Attributes:
        permission_classes: IsAuthenticated
        serializer_class: UserSerializer

    Methods:
        get_queryset(self): Returns either the Followers or Following list
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        """Will returns a contacts list.

        Returns either the current user's followers or following list.

            Request Data:
                type(string): Need to be either followers or following
                    Will default to followers if not provided or invalid
            Returns List: All followers or following
        """
        try:
            user = CustomUser.objects.get(id=self.request.user.id)
            if self.request.data['type'] == 'followers':
                return user.followers.all()
            elif self.request.data['type'] == 'following':
                return user.following.all()
            else:
                raise KeyError('Invalid type')
        except KeyError:
            return user.followers.all()
