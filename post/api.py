from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer


class PostAPI(ModelViewSet):
    'Retrieves posts via ModelViewSet. Allows access to all.'
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
