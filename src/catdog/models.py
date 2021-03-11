from django.db import models

# Create your models here.


class AnimalImage(models.Model):
    url = models.URLField()
    species = models.CharField(max_length=10)
    data_crate = models.DateTimeField()
    image_type = models.CharField(max_length=10)
