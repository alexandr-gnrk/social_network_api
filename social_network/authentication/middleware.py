from django.utils import timezone
from django.contrib.auth import get_user_model


class LastSeenUserMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            get_user_model().objects.\
                filter(pk=request.user.pk).\
                update(last_seen=timezone.now())

        return self.get_response(request)
