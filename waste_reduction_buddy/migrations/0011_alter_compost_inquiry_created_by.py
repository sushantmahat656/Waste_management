# Generated by Django 4.2.6 on 2024-02-23 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('waste_reduction_buddy', '0010_remove_appointment_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compost_inquiry',
            name='Created_By',
            field=models.ForeignKey(default='User Not logged in', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
