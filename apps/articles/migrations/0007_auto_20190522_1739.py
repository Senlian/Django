# Generated by Django 2.2 on 2019-05-22 17:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0006_auto_20190522_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecolumns',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 17, 39, 44, 536000), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 17, 39, 44, 537000), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='articletags',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 17, 39, 44, 536000), verbose_name='创建时间'),
        ),
        migrations.CreateModel(
            name='ArticleComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.Articles')),
                ('author', models.ForeignKey(on_delete=models.SET('未知用户'), related_name='comments', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
                'db_table': 'articlecomments',
                'ordering': ['-created'],
            },
        ),
    ]