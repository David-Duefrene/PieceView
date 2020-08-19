"""Serializers for the post module"""
from rest_framework import serializers

from account.models import CustomUser
from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for showing the author of a post"""

    class Meta:
        """The Meta

        Attributes:
            model: CustomerUser
            fields: username, first_name, last_name, is_staff, is_active,
                    date_joined, photo_link, get_absolute_url
        """

        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'is_staff', 'is_active',
            'date_joined', 'photo_link', 'get_absolute_url'
        ]


class PostSerializer(serializers.ModelSerializer):
    """Serializer for showing a post"""

    authors = AuthorSerializer()

    class Meta:
        """The Meta

        Attributes:
            model: Post
            fields: authors, content, title, created, get_absolute_url,
        """

        model = Post
        fields = ['authors', 'content', 'title', 'created', 'get_absolute_url']


class PostPreviewSerializer(serializers.ModelSerializer):
    """Serializer for showing a post preview"""

    authors = AuthorSerializer()

    class Meta:
        """The Meta

        Attributes:
            model: Post
            fields: authors, summary, title, created, get_absolute_url,
        """

        model = Post
        fields = ['authors', 'summary', 'title', 'created', 'get_absolute_url']
