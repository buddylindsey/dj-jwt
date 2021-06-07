from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin

from rest_framework_simplejwt.authentication import JWTAuthentication


class DjangoJWTAuthentication(JWTAuthentication, MiddlewareMixin):
    def __call__(self, request):
        if hasattr(request, "user") and not isinstance(request.user, AnonymousUser):
            return self.get_response(request)

        auth_user = self.authenticate(request)
        if isinstance(auth_user, tuple):
            request.user = auth_user[0]
        elif auth_user:
            request.user = auth_user
        else:
            request.user = AnonymousUser()

        return self.get_response(request)
