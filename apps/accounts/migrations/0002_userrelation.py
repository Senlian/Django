# Generated by Django 2.2 on 2019-05-27 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fans', to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='粉丝')),
                ('focus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='focus', to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='关注')),
            ],
            options={
                'verbose_name': '用户关系',
                'verbose_name_plural': '用户关系',
                'db_table': 'userrelation',
            },
        ),
    ]
