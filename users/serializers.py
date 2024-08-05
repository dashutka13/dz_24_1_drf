from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import User, Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    payment_list = SerializerMethodField()

    def get_payment_list(self, user):
        return [(payment.date_of_payment, payment.payment_amount) for payment in Payment.objects.filter(user=user)]

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
