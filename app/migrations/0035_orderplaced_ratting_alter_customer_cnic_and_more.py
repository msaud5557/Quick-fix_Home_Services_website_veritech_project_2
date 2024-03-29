# Generated by Django 4.0.4 on 2022-05-29 04:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_alter_customer_city_alter_services_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='ratting',
            field=models.CharField(choices=[('Poor', 'Poor'), ('Avrage', 'Avrage'), ('Good', 'Good'), ('Excellient', 'Excellient')], default='pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Cnic',
            field=models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{13}$', 'Only 13 number are allowed.')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postelcode',
            field=models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{5}$', 'Only 5 nuber are allowed.')]),
        ),
        migrations.AlterField(
            model_name='services',
            name='Cnic',
            field=models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{13}$', 'Only 13 number are allowed.')]),
        ),
    ]
