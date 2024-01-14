# Generated by Django 4.0.4 on 2022-05-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_expence_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='country',
        ),
        migrations.AddField(
            model_name='customer',
            name='postelcode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name=1),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Punjab', 'Punjab'), ('Sindh', 'Sindh'), ('Khyber Pakhtunkhwa', 'Khyber Pakhtunkhwa'), ('Gilgit-Baltistan', 'Gilgit-Baltistan'), ('Islamabad Capital Territory', 'Islamabad Capital Territory'), ('Balochistan', 'Balochistan')], max_length=200),
        ),
    ]
