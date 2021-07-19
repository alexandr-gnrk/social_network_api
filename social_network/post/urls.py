from django.urls import path
from .views import PostList, PostDetail, post_like, post_unlike

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('<int:pk>/like/', post_like),
    path('<int:pk>/unlike/', post_unlike),
]