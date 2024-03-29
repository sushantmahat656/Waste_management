# Generated by Django 5.0.2 on 2024-03-11 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste_reduction_buddy', '0023_alter_appointment_appointment_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(default=datetime.time(14, 24, 17, 551243)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='selling_option',
            field=models.CharField(blank=True, choices=[('sell', 'Sell'), ('donate', 'Donate')], max_length=10, null=True),
        ),
    ]
