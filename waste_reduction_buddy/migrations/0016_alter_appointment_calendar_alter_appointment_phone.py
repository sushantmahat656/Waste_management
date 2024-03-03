# Generated by Django 4.2.6 on 2024-02-26 06:39

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste_reduction_buddy', '0015_alter_appointment_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='calendar',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator('^[0-9]*$', message='Phone number must contain only digits.')]),
        ),
    ]