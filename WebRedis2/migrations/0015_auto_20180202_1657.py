# Generated by Django 2.0 on 2018-02-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebRedis', '0014_auto_20180202_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbserver',
            name='status',
            field=models.CharField(choices=[('T', '正常'), ('F', '异常')], default='T', max_length=64, verbose_name='状态'),
        ),
    ]
