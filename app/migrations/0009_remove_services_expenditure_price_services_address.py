# Generated by Django 4.0.4 on 2022-05-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_services_actual_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='expenditure_price',
        ),
        migrations.AddField(
            model_name='services',
            name='address',
            field=models.CharField(default=0, max_length=200),
        ),
    ]