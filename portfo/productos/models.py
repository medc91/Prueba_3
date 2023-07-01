from django.db import models

# Create your models here.
class Productos(models.Model):
  codigo = models.IntegerField()
  nombre = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=200)
  imagen = models.CharField(max_length=1000)
  precio = models.IntegerField(null=True)
