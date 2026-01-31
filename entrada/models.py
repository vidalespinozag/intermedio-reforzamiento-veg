from django.db import models

from funcion.models import Funcion


# Create your models here.

class Entrada(models.Model):
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
    asiento = models.CharField(max_length=3)
    vendido = models.BooleanField(default=True)