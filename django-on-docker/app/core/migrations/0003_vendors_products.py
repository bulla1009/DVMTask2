# Generated by Django 4.1 on 2023-05-21 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendors',
            name='products',
            field=models.ManyToManyField(to='core.product'),
        ),
    ]
