# Generated by Django 3.0.8 on 2020-08-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_auto_20200429_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
