# Generated by Django 4.0.4 on 2022-05-29 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_orderplaced_ratting_alter_customer_cnic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='statuscus',
            field=models.CharField(choices=[('Service is Complete', 'Service is Complete'), ('Service is Complete', 'Service is Complete')], default='In progress', max_length=100),
        ),
    ]
