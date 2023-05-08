from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=(255),
        verbose_name="Название сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to="logo/"
    )
    photo = models.ImageField(
        upload_to="photo_image_index/",
        verbose_name="Обои на страницу"
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"