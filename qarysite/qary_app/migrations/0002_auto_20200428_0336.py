# Generated by Django 3.0.2 on 2020-04-28 03:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qary_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 3, 35, 50, 818500, tzinfo=utc)),
        ),
    ]
