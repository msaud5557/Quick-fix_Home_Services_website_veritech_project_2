# Generated by Django 4.0.4 on 2022-05-21 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_services_mobile_no_alter_services_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='address',
            field=models.CharField(default='abc', max_length=200),
        ),
    ]
