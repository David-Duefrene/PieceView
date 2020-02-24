from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import CustomUser, Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'photo', 'first_name', 'last_name',
                  'followers', 'photo_url', 'get_absolute_url']


class ContactSerializer(serializers.ModelSerializer):
    from_user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    to_user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Contact
        fields = ['from_user', 'to_user', 'created']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'first_name',
                  'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
