# Generated by Django 2.1.4 on 2019-07-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hr',
            name='average_montly_hours',
            field=models.FloatField(default=0),
        ),
    ]
