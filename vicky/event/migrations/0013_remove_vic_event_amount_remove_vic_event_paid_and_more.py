# Generated by Django 5.0.7 on 2024-09-21 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_remove_vic_event_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vic_event',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='vic_event',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='vic_event',
            name='payment_id',
        ),
    ]