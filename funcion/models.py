from django.db import models

from pelicula.models import Pelicula


# Create your models here.

class Funcion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    fecha_horario = models.DateTimeField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.CharField(max_length=30)