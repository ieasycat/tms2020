from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    counter = models.IntegerField()
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.pk} - {self.name} - ' \
               f'{self.price} - {self.counter} - {self.comment}'
