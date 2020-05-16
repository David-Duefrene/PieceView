from rest_framework.generics import RetrieveAPIView

from .models import Post
from .serializers import PostSerializer


class PostAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj
