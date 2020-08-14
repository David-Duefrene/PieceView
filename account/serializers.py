"""Serializers for the Account module."""
from django.contrib.auth import authenticate, get_user_model

from rest_framework import serializers

from .models import CustomUser, Contact
User = get_user_model()


class ContactUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'biography',
                  'photo_url', 'get_absolute_url']


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']


class UserSerializer(serializers.ModelSerializer):
    """Serializer for showing a user's data."""

    following = FollowingSerializer(many=True)

    class Meta:
        """The Meta

        Attributes:
            Model: CustomUser
            Fields: username, email, photo, first_name, last_name, followers,
                photo_url, get_absolute_url
        """

        model = CustomUser
        fields = ['username', 'email', 'photo', 'first_name', 'last_name',
                  'biography', 'photo_url', 'get_absolute_url', 'following']
        depth = 1


class UserEditSerializer(serializers.ModelSerializer):
    """Serializer for editing a user's data."""

    class Meta:
        """The Meta

        Attributes:
                Model: CustomUser
                photo(FileField): The user's photo, not required
                Fields: email, first_name, last_name, photo_link
        """

        model = CustomUser
        photo = serializers.FileField(required=False)
        fields = ['email', 'first_name', 'last_name', 'photo_link',
                  'biography']


class ContactSerializer(serializers.ModelSerializer):
    """Serializer for a user's contacts list

    Attributes:
        from_user(PrimaryKeyRelatedField) -- The user who started to follow
        to_user(PrimaryKeyRelatedField): The user who is being followed
    """

    from_user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    to_user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        """The Meta

        Attributes:
            Model: Contact
            Fields: from_user, to_user, created
        """

        model = Contact
        fields = ['from_user', 'to_user', 'created']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer to register a user"""

    class Meta:
        """The Meta

        Attribute:
            Model: User
            first_name(CharField): User's first name
            last_name(CharField): User's last name
            Fields: username, email, password, first_name, last_name
            extra_kwargs = {'password': {'write_only': True}}
        """

        model = User
        first_name = serializers.CharField(required=False)
        last_name = serializers.CharField(required=False)
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    """Serializer to log a user in

    Attributes:
        username(CharField): The user's username
        password(CharField): The user's password
    """

    username = serializers.CharField()
    password = serializers.CharField()

    @staticmethod
    def validate(data):
        """Validate the user data"""
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
