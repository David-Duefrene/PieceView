from django.contrib.auth.models import Group

from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'groups', 'photo',
                  'first_name', 'last_name']
