# Generated by Django 4.2.1 on 2023-06-01 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_rename_descriptions_osp_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='osp',
            name='parent_images',
        ),
        migrations.AddField(
            model_name='osp',
            name='parent_image',
            field=models.ImageField(blank=True, null=True, upload_to='parent_imageS/', verbose_name='Ваша фото'),
        ),
    ]
