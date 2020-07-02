from django.core.paginator import Paginator

from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from .models import Post
from .serializers import PostSerializer


class PostAPI(ListCreateAPIView):
    """Handles posts. Allows view access to all but will restrict
    creating/editing a post to an authenticated user.

    Attributes:
        queryset: Current query set is all Posts
        permission_classes: Sets non-authenticated users to read only
        serializer_class: Uses PostSerializer

    Methods:
        post(self, request, *args, **kwargs): Allows a authenticated user to
        create a post
    """
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        """Post function for the PostAPI. Takes in the request from the user.
            User needs authentication token.

            Request Data:
                title (string): The title of the post
                content (string): The post itself.

            Return Response:
                status (string): The status of the post submitted
                URL (string): CONDITIONAL will only appear if status is
                    a success
        """
        try:
            author = request.user
            new_posts = Post.objects.create(
                authors=author,
                title=request.data['title'],
                content=request.data['content']
            )
            return Response({
                'status': 'Success! Post created',
                'URL': new_posts.get_absolute_url()
            })
        except KeyError as error:
            return Response({'Error': str(error) + ' cannot be None'})
