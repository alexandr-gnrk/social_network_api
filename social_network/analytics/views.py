from django.db.models import Count
from rest_framework import generics, permissions
from post.models import Like
from .serializers import LikesByDaySerializer
from .filters import LikesByDayFilter


class LikesByDay(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = LikesByDaySerializer
    filter_class = LikesByDayFilter

    def get_queryset(self):
        return Like.objects.\
            values('date').\
            annotate(likes=Count('date')).\
            order_by()
