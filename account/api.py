from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView

from knox.models import AuthToken

from .models import CustomUser
from .serializers import (
    UserSerializer, LoginSerializer, RegisterSerializer, UserEditSerializer
)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
          "user": UserSerializer(
            user, context=self.get_serializer_context()).data,
          "token": AuthToken.objects.create(user)[1]
        })


class EditProfileAPI(RetrieveUpdateAPIView):
    serializer_class = UserEditSerializer

    def get_queryset(self):
        user = self.request.user
        return user

    def get_object(self):
        obj = self.request.user
        return obj


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class LoginAPI(generics.GenericAPIView):
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


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ContactsAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        user = CustomUser.objects.get(id=self.request.user.id)
        return user.followers.all()
