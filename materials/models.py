from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=250, verbose_name="Название курса", help_text="Введите название курса"
    )
    preview = models.ImageField(upload_to='materials/courses', verbose_name='Превью', help_text='Загрузите картинку',
                                blank=True, null=True)
    description = models.TextField(verbose_name='Описание курса', help_text='Введите описание курса', blank=True,
                                   null=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(
        max_length=250, verbose_name="Название урока", help_text="Введите название урока"
    )
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Курс', help_text='Укажите курс',
                               blank=True, null=True)
    preview = models.ImageField(upload_to='materials/lessons', verbose_name='Превью', help_text='Загрузите картинку',
                                blank=True, null=True)
    description = models.TextField(verbose_name='Описание урока', help_text='Введите описание урока', blank=True,
                                   null=True)
    video_url = models.URLField(max_length=250, verbose_name='Ссылка на видео', help_text='Укажите ссылку на видео',
                                blank=True, null=True)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
