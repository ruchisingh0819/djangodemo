from django.db import models

# Create your models here.
class Index1(models.Model):
    def __str__(self):
        return self.name
