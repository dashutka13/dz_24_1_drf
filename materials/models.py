from django.conf import settings
from django.db import models


class Course(models.Model):
    course_name = models.CharField(
        max_length=250,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="materials/courses",
        verbose_name="Превью",
        help_text="Загрузите картинку",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Введите описание курса",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
                              verbose_name="Владелец",
                              help_text="Укажите владельца")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    lesson_name = models.CharField(
        max_length=250,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Укажите курс",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="materials/lessons",
        verbose_name="Превью",
        help_text="Загрузите картинку",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание урока",
        help_text="Введите описание урока",
        blank=True,
        null=True,
    )
    video_url = models.URLField(
        max_length=250,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
                              verbose_name="Владелец",
                              help_text="Укажите владельца")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Подписчик")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", blank=True, null=True)

    def __str__(self):
        return f'{self.course}: {self.user}'

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
