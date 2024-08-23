from celery import shared_task
from django.core.mail import send_mail

from config import settings
from materials.models import Course, Subscription
from users.models import User


@shared_task
def send_update_email(course_pk):
    course = Course.objects.filter(pk=course_pk).first()
    users = User.objects.all()
    for user in users:
        subscription = Subscription.objects.filter(
            course=course_pk, user=user.pk
        ).first()
        if subscription:
            send_mail(
                subject=f'Курс"{course.course_name}"',
                message=f'Курс "{course.course_name}" обновился!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
