# Generated by Django 5.0.2 on 2024-03-11 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste_reduction_buddy', '0022_appointment_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(default=datetime.time(14, 20, 18, 704478)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='selling_option',
            field=models.CharField(blank=True, choices=[('SELL', 'Sell'), ('DONATE', 'Donate')], max_length=10, null=True),
        ),
    ]
