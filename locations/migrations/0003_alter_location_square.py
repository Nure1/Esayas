# Generated by Django 4.2.2 on 2023-06-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_location_latitude_location_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='square',
            field=models.FloatField(null=True),
        ),
    ]
