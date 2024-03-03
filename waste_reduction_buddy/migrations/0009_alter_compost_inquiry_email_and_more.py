# Generated by Django 4.2.6 on 2024-02-05 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste_reduction_buddy', '0008_compost_inquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compost_inquiry',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='compost_inquiry',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='compost_inquiry',
            name='message',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='compost_inquiry',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='compost_inquiry',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]