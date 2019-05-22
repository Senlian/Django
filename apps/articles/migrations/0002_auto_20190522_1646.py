# Generated by Django 2.2 on 2019-05-22 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecolumns',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 16, 46, 59, 702000), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 16, 46, 59, 703000), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, verbose_name='访问地址'),
        ),
        migrations.AlterField(
            model_name='articletags',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 16, 46, 59, 703000), verbose_name='创建时间'),
        ),
    ]