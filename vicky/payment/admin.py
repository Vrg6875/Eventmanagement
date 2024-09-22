from django.contrib import admin
from payment.models import vic_payment

class vic_payment_admin(admin.ModelAdmin):
    list_display=('amount','payment_id','paid')


admin.site.register(vic_payment, vic_payment_admin)   
