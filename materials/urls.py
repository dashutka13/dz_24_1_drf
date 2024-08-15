from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import SimpleRouter

from materials.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView, SubscriptionCreateAPIView,
)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
                  path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
                  path("lesson/", LessonListAPIView.as_view(), name="lesson"),
                  path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-retrieve"),
                  path(
                      "lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson-update"
                  ),
                  path(
                      "lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson-delete"
                  ),
                  path("subscription/", SubscriptionCreateAPIView.as_view(), name="subscription")
              ] + router.urls
