# Generated by Django 2.2 on 2019-05-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='邮箱'),
        ),
    ]