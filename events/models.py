from django.db import models
from departments.models import Department

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(verbose_name='Agendado para: ')
    objective = models.CharField(max_length=500)
    description = models.TextField()
    departtmet_id = models.ManyToManyField(Department, related_name='departments_id')


    def __str__(self):
        return self.name