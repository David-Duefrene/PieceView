from django.contrib.auth import authenticate, get_user_model

from rest_framework import serializers

from .models import CustomUser, Contact
User = get_user_model()


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
        model = User
        first_name = serializers.CharField(required=False)
        last_name = serializers.CharField(required=False)
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    @staticmethod
    def validate(data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
