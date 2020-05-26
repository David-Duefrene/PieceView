from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    GenericAPIView, UpdateAPIView, RetrieveAPIView
)
from django.contrib.auth.hashers import make_password

from knox.models import AuthToken

from .models import CustomUser
from .serializers import (
    UserSerializer, LoginSerializer, RegisterSerializer, UserEditSerializer
)


class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):

        hashedPass = make_password(request.data['password'])
        request.data['password'] = hashedPass

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
          "user": UserSerializer(
            user, context=self.get_serializer_context()).data,
          "token": AuthToken.objects.create(user)[1]
        })


class EditProfileAPI(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserEditSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.first_name = request.data['first_name']
        instance.last_name = request.data['last_name']
        instance.email = request.data['email']
        instance.save()

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        return Response(serializer.data)

    # To avoid needing a pk in the URL or a lookup_field
    def get_object(self):
        obj = self.request.user
        return CustomUser.objects.get(username=obj.username)


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


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


class UserAPI(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ContactsAPI(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        user = CustomUser.objects.get(id=self.request.user.id)
        return user.followers.all()
