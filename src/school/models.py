from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Diary(models.Model):
    average_score = models.FloatField()
    student = models.OneToOneField(
        'Student',
        null=True,
        on_delete=models.SET_NULL,
        related_name='diary'
    )

    def __str__(self):
        return f'{self.pk} - {self.student.firstname} - {self.student.lastname} - {self.student.group.name} - {self.average_score}'


class Student(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    group = models.ForeignKey(
        Group,
        null=True,
        on_delete=models.SET_NULL,
        related_name='students',
    )

    def __str__(self):
        return f'{self.pk} - {self.firstname} - {self.lastname} - {self.group.name}'
