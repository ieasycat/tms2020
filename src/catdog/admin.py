from django.contrib import admin
from django.contrib.admin import ModelAdmin

from catdog.models import AnimalImage

# Register your models here.


class AnimalImageAdmin(ModelAdmin):
    list_display = [
        'id',
        'url',
        'species',
        'data_crate',
        'image_type',
    ]


admin.site.register(AnimalImage, AnimalImageAdmin)
