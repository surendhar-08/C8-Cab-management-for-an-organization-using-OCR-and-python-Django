# Generated by Django 3.1.7 on 2021-03-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NumberPlateDetector', '0002_auto_20210309_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetails',
            name='car_number',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
