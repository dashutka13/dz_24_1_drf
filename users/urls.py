from django.urls import path

from users.apps import UsersConfig
from rest_framework.routers import SimpleRouter

from users.views import UserViewSet, PaymentListAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", UserViewSet)

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name="payment"),
              ] + router.urls
