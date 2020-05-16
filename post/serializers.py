from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['authors', 'content', 'title', 'created', 'get_absolute_url']
