from django.contrib.auth import get_user, get_user_model

from django.core.management.base import BaseCommand
from rest_framework_simplejwt.tokens import RefreshToken


class Command(BaseCommand):
    help = "Create an access and refresh token for testing"

    def add_arguments(self, parser):
        parser.add_argument(
            "--email", type=str, help="Email address of user to create jwt for"
        )
        parser.add_argument("--userid", type=int, help="ID of user to create jwt for")

    def handle(self, *args, **options):
        User = get_user_model()

        email = options.get("email")
        user_id = options.get("userid")

        try:
            if user_id:
                user = User.objects.get(id=user_id)
            elif email:
                user = User.objects.get(email=email)
            else:
                user = User.objects.first()
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR("User does not exist or no Users in system")
            )
            return

        refresh_token = RefreshToken.for_user(user)

        self.stdout.write(
            self.style.SUCCESS(
                f"Tokens for: {user.first_name} {user.last_name} <{user.email}>"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(f"Access Token:  {str(refresh_token.access_token)}")
        )
        self.stdout.write(self.style.SUCCESS(f"Refresh Token: {str(refresh_token)}"))