from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription

from materials.validators import VideoUrlValidator


class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = SerializerMethodField()
    subscriber = SerializerMethodField()

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        return [lesson.lesson_name for lesson in Lesson.objects.filter(course=course)]

    def get_subscriber(self, course):
        if Subscription.objects.filter(course=course).exists():
            return True
        return False

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoUrlValidator(field='video_url')]


class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
