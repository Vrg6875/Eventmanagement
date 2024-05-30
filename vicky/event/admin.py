from django.contrib import admin
from event.models import vic_event, vic_register,vic_contact

class vic_event_admin(admin.ModelAdmin):
    list_display=('event_name', 'event_date', 'event_description', 'event_category', 'guests','email','state','city','your_name')

class vic_register_admin(admin.ModelAdmin):
    list_display=('fiest_name', 'last_name', 'password1','password2','username')

class vic_contact_admin(admin.ModelAdmin):
    list_display=('name', 'email')

admin.site.register(vic_event, vic_event_admin)   
admin.site.register(vic_register, vic_register_admin)
admin.site.register(vic_contact, vic_contact_admin)
