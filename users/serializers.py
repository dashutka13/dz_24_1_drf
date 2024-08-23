from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Subscription
from materials.serializers import CourseSerializer
from users.models import Payment, User


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    payment_list = SerializerMethodField()
    subscription = SerializerMethodField()

    def get_payment_list(self, user):
        return [
            (payment.date_of_payment, payment.payment_amount)
            for payment in Payment.objects.filter(user=user)
        ]

    def get_subscription(self, user):
        if Subscription.objects.filter(user=user).exists():
            return Subscription.objects.get(user=user).course.course_name

    class Meta:
        model = User
        fields = "__all__"


# class UserNotOwnerSerializer(ModelSerializer):
#     """
#     Пыталась решить задание со * из 25_1 ничего не вышло
#     """
#     class Meta:
#         model = User
#         fields = "__all__"
