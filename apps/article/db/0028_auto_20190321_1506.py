# Generated by Django 2.1.7 on 2019-03-21 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0027_auto_20190321_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 15, 6, 14, 32000)),
        ),
    ]
