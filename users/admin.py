from django.contrib import admin

from users.models import Payment, User


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_payment', 'paid_lesson', 'paid_course',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'city', 'phone',)
