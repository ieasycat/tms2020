from django.db import models

# Create your models here.


class Customer(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    age = models.IntegerField()
    profession = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.pk} - {self.firstname} - ' \
               f'{self.lastname} - {self.age} - ' \
               f'{self.profession}'
