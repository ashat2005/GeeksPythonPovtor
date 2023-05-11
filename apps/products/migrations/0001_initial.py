# Generated by Django 4.2.1 on 2023-05-10 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_currency', models.CharField(max_length=50, verbose_name='Название валюты')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('description', models.CharField(max_length=300, verbose_name='Описание продукта')),
                ('product_image', models.ImageField(upload_to='product_images/', verbose_name='Фотография продукта')),
                ('price', models.PositiveBigIntegerField(verbose_name='Цена')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_currency', to='products.currency', verbose_name='Название валюты')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]