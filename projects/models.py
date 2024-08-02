from django.db import models
from departments.models import Department

class Project(models.Model):
    name = models.CharField(max_length=200)
    department_id = models.ManyToManyField(Department, related_name='departmant_org')
    description = models.TextField()
    objective = models.CharField(max_length=500)

    def __str__(self):
        return self.name