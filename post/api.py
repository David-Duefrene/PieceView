"""Handles the post model."""
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from .models import Post
from .serializers import PostSerializer, PostPreviewSerializer
from account.models import CustomUser
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

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostPreviewSerializer

    def get_queryset(self):
        """Will returns a QuerySet of posts

        Returns either the posts of the current user's following list or all
        posts.

            Request Parameters:
                type(string): Need to be either following or all
                    Will default to all if not provided or invalid
            Returns List: Posts of users following list or All posts
        """
        try:
            user = CustomUser.objects.get(id=self.request.user.id)
            if self.request.GET.get('type', '') == 'following':
                following_list = user.following.all()
                posts = Post.objects.none()
                for author in following_list:
                    posts = posts | Post.objects.filter(owner_id=author.id)
                return posts
            elif self.request.GET.get('type', '') == 'all':
                return Post.objects.all()
            else:
                raise KeyError('Invalid type')
        except KeyError:
            return Post.objects.all()
        except CustomUser.DoesNotExist:
            return Post.objects.all()

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
