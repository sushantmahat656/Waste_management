# Generated by Django 5.0.2 on 2024-03-25 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste_reduction_buddy', '0028_alter_appointment_appointment_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='Created_By',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(default=datetime.time(11, 51, 49, 69627)),
        ),
    ]
