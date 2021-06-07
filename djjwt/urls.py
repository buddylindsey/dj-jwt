from django.urls import path

from .views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # Exclude as not appropriate for this app?
    # path('admin/', admin.site.urls),
    path("authenticate/", TokenObtainPairView.as_view(), name="authenticate"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("verify/", TokenVerifyView.as_view(), name="verify"),
]
