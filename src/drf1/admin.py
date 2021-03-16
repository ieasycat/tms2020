from django.contrib import admin
from drf1.models import Product
from django.contrib.admin import ModelAdmin

# Register your models here.


class ProductAdmin(ModelAdmin):
    list_display = [
        'id',
        'name',
        'price',
        'counter',
        'comment',
    ]


admin.site.register(Product, ProductAdmin)
