# Generated by Django 2.1.7 on 2019-03-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20190327_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuserprofilemodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='头像'),
        ),
    ]