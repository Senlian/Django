# Generated by Django 2.1.7 on 2019-03-27 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190327_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuserdetailmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.AccountUserProfileModel', to_field='user_id', verbose_name='账户'),
        ),
    ]
