from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .serializers import UserActivitySerializer


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_activity(request):
    user = get_user_model().objects.\
        get(pk=request.user.pk)


    serializer = UserActivitySerializer(user)
    return JsonResponse(serializer.data)