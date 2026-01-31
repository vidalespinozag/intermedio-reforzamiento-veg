from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=50,blank=True,
    null=True)
    duracion = models.IntegerField(default=0)
    clasificacion = models.CharField(max_length=80)