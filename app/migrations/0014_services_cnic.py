# Generated by Django 4.0.4 on 2022-05-21 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_services_as_per_services_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='Cnic',
            field=models.CharField(default=0, max_length=13),
        ),
    ]
