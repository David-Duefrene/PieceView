"""Handles the post model."""
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from .models import Post
from .serializers import PostSerializer
from common.permissions import IsOwnerOrReadOnly


class PostListAPI(ListCreateAPIView):
    """Retrieves posts Lists and allows creating a post.

    Allows view access to all but
    will restrict creating a post to an authenticated user.

    Attributes:
        queryset: Current query set is all Posts
        permission_classes: Sets non-authenticated users to read only
        serializer_class: Uses PostSerializer

    Methods:
        post(self, request, *args, **kwargs): Allows a authenticated user to
            create a post.
    """

    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        """Will retrieves a list of posts.

        Allow unauthenticated access and is paginated by ?page=num in the URL.
        No data needed in the request.

            Return Response:
                Returns the same as default get, it just trims the content to
                a 3000 character preview.
        """
        data = super().get(request, *args, **kwargs)
        results = data.data['results']
        for post in results:
            # Trim the content down to a preview.
            preview = post['content'][0:3000]
            post['content'] = preview
        return data

    def post(self, request, *args, **kwargs):
        """Post function for the PostAPI.

        Takes in the request from the user. User needs authentication token.

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


class PostAPI(RetrieveUpdateDestroyAPIView):
    """Handles individual posts.

    Allows view access to all but will restrict editing a post to an
    authenticated user. Deleting a post should only be allowed by admin,
    staff, or the creator of the post.

    Attributes:
        queryset: Current query set is all Posts
        permission_classes: Sets non-authenticated users to read only
        serializer_class: Uses PostSerializer
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
