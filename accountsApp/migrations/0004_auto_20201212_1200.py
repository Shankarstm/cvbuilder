# Generated by Django 3.1.2 on 2020-12-12 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountsApp', '0003_auto_20201212_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='toppings',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]
