from django.core.management import BaseCommand

from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        Payment.objects.all().delete()

        user_list = [
            {"pk": 1, "email": "mouse@gmail.com", "city": "SPB"},
            {"pk": 2, "email": "cat@gmail.com", "city": "MSK"},
        ]

        payment_list = [
            {
                "user": 1,
                "date_of_payment": "2024-01-15",
                "payment_amount": "15000",
                "payment_method": "cash",
                "paid_course": "DRF",
                "paid_lesson": "100",
            },
            {
                "user": 2,
                "date_of_payment": "2024-03-17",
                "payment_amount": "25000",
                "payment_method": "card",
                "paid_course": "Django",
                "paid_lesson": "200",
            },
        ]

        for payment_item in payment_list:
            Payment.objects.create(**payment_item)
