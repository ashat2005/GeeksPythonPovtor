# Generated by Django 4.2.1 on 2023-05-18 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Info',
        ),
    ]
