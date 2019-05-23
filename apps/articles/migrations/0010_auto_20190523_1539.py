# Generated by Django 2.2 on 2019-05-23 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20190523_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecolumns',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='articlecomments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.Articles', verbose_name='文章'),
        ),
        migrations.AlterField(
            model_name='articlecomments',
            name='author',
            field=models.ForeignKey(on_delete=models.SET('未知用户'), related_name='comments', to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='articlecomments',
            name='body',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='articlecomments',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='articletags',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]
