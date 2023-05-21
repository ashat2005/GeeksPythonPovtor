from django.contrib import admin
from apps.products.models import Products, Currency
# Register your models here.
class ProductsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
admin.site.register(Products, ProductsFilterAdmin)
admin.site.register(Currency)