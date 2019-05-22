# Generated by Django 2.2 on 2019-05-22 17:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190522_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecolumns',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 17, 19, 37, 562000), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='column',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to='articles.ArticleColumns', verbose_name='栏目'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 17, 19, 37, 563000), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='favorites',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='article_favorites', to=settings.AUTH_USER_MODEL, verbose_name='收藏'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='article_likes', to=settings.AUTH_USER_MODEL, verbose_name='点赞'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='article_tags', to='articles.ArticleTags', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='articletags',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 17, 19, 37, 563000), verbose_name='创建时间'),
        ),
    ]
