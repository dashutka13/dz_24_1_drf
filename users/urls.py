from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from rest_framework.routers import SimpleRouter

from users.views import UserViewSet, PaymentListAPIView, PaymentCreateAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", UserViewSet)

urlpatterns = [
                  path('payment/', PaymentListAPIView.as_view(), name="payment"),
                  path('payment/create/', PaymentCreateAPIView.as_view(), name="payment_create"),
                  path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
                  path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh')
              ] + router.urls
