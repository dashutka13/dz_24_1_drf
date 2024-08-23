from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from users.services import (stripe_create_price, stripe_create_product,
                            stripe_create_session)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_serializer_class(self):
    #     """
    #     Пыталась решить задание со * из 25_1 ничего не вышло
    #     """
    #     if self.request.user != self.request.user.is_authenticated:
    #         return UserNotOwnerSerializer
    #     return UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsAuthenticated,)
        return super().get_permissions()


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]

    filterset_fields = (
        "payment_method",
        "paid_course",
        "paid_lesson",
    )
    ordering_fields = ("date_of_payment",)


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product = stripe_create_product(payment.paid_course)
        price = stripe_create_price(product=product, amount=payment.payment_amount)
        session_id, session_url = stripe_create_session(price)
        payment.id_session = session_id
        payment.link_to_pay = session_url
        payment.save()
