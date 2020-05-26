from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import CustomUser, Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'photo', 'first_name', 'last_name',
                  'followers', 'photo_url', 'get_absolute_url']


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        photo = serializers.FileField(required=False)
        fields = ['email', 'first_name', 'last_name']


class ContactSerializer(serializers.ModelSerializer):
    from_user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    to_user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Contact
        fields = ['from_user', 'to_user', 'created']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        first_name = serializers.CharField(required=False)
        last_name = serializers.CharField(required=False)
        fields = ('id', 'username', 'email', 'password')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    @staticmethod
    def validate(data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
