# Generated by Django 5.0.2 on 2024-04-02 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste_reduction_buddy', '0031_alter_appointment_appointment_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(default=datetime.time(12, 6, 45, 845569)),
        ),
    ]
