# Generated by Django 4.2.13 on 2024-06-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_remove_vic_event_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vic_event',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vic_event',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='vic_event',
            name='event_category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vic_event',
            name='event_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vic_event',
            name='guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vic_event',
            name='state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vic_event',
            name='your_name',
            field=models.CharField(max_length=50),
        ),
    ]
