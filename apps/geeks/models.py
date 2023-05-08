from django.db import models

# Create your models here.
class Geeks(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Курсы"
    )
    course_photo = models.ImageField(
        upload_to= 'product_images/',
        verbose_name="Фотография продукта"
    )
    