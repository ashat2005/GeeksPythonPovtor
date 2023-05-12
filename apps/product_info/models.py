from django.db import models

# Create your models here.
class ProductInfo(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Все курсы"
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"