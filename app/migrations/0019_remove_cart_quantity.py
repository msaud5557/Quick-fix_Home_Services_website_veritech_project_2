# Generated by Django 4.0.4 on 2022-05-22 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_services_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]
