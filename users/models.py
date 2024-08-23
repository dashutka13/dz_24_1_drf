from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Введите почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Укажите номер телефона",
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        help_text="Укажите город",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    CHOICES = (
        ("cash", "наличные"),
        ("card", "карта"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    date_of_payment = models.DateField(verbose_name="Дата оплаты")
    payment_amount = models.IntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(
        max_length=100, choices=CHOICES, verbose_name="Способ оплаты"
    )
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс"
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок"
    )
    id_session = models.CharField(
        max_length=255, verbose_name="Id сессии", blank=True, null=True
    )
    link_to_pay = models.URLField(
        max_length=400, verbose_name="Ссылка на оплату", blank=True, null=True
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
