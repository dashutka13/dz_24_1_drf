from users.apps import UsersConfig
from rest_framework.routers import SimpleRouter

from users.views import UserViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [

] + router.urls
