from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination

from django.contrib.auth.hashers import make_password

from knox.models import AuthToken

from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer


class UserAPI(ModelViewSet):
    """API to allow a user to create, edit and delete account.
    """
    PageNumberPagination.page_size = 5
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        if request.data['password'] is not None:
            hashedPass = make_password(request.data['password'])
            request.data['password'] = hashedPass

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
          "user": UserSerializer(
            user, context=self.get_serializer_context()).data,
          "token": AuthToken.objects.create(user)[1]
        })

    def update(self, request, *args, **kwargs):
        instance = request.user
        instance.first_name = request.data['first_name']
        instance.last_name = request.data['last_name']
        instance.email = request.data['email']
        instance.save()

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        return Response(serializer.data)


class LoginAPI(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
            "user": UserSerializer(
                user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class ContactsAPI(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
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
