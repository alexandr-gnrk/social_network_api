from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer