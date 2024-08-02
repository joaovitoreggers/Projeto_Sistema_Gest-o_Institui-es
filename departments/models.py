from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.ManyToManyField(User, related_name='accounts')
    responsabilitys = models.CharField(max_length=1100)

    def __str__(self):
        return self.name
