from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from users.views import UsersApiViewSet, UserView

router_users = DefaultRouter()
router_users.register(
    viewset=UsersApiViewSet,
    basename="usuarios",
    prefix="usuarios"
)

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view()),
    path('auth/me', UserView.as_view())
]
