# Generated by Django 3.1 on 2020-08-09 15:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20200809_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 15, 14, 37, 155344, tzinfo=utc)),
        ),
    ]