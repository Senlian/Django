# Generated by Django 2.2 on 2019-05-24 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20190524_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='status',
            field=models.CharField(choices=[(1, '公开'), (2, '私密'), (3, '草稿'), (4, '删除')], default=1, max_length=5, verbose_name='状态'),
        ),
    ]
