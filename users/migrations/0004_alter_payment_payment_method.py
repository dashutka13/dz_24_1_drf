# Generated by Django 5.0.7 on 2024-07-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_payment_payment_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(
                choices=[("cash", "наличные"), ("card", "карта")],
                max_length=100,
                verbose_name="Способ оплаты",
            ),
        ),
    ]
