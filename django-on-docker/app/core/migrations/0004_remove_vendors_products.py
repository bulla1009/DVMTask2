# Generated by Django 4.1 on 2023-05-21 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_vendors_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendors',
            name='products',
        ),
    ]
