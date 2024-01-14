# Generated by Django 4.0.4 on 2022-05-22 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_services_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='Employee',
            field=models.CharField(choices=[('Electrician', 'Electrician'), ('Plumber', 'Plumber'), ('Sweaper', 'Sweaper'), ('Carpenter', 'Carpenter'), ('Drain clean', 'Drain clean'), ('AC repair', 'AC repair'), ('Painting & Decorating', 'Painting & Decorating')], default='abc', max_length=100),
        ),
    ]
