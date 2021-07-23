from django.urls import path
from .views import LikesByDay


urlpatterns = [
    path('', LikesByDay.as_view())
]