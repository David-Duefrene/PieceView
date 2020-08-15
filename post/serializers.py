from rest_framework import serializers

from account.models import CustomUser
from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'is_staff', 'is_active',
            'date_joined', 'photo_link',
        ]


class PostSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer()

    class Meta:
        model = Post
        fields = ['authors', 'content', 'title', 'created', 'get_absolute_url']
        depth = 1
