from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
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


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_like(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user

    if user not in post.users_like.all():
        post.users_like.add(user)
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_409_CONFLICT)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_unlike(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user

    if user in post.users_like.all():
        post.users_like.remove(user)
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_409_CONFLICT) 