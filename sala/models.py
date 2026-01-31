from django.db import models

# Create your models here.

class Sala(models.Model):
    nombre = models.CharField(max_length=30)
    capacidad = models.IntegerField(default=0)