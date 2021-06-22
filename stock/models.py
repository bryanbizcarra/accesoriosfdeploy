from django.db import models
from datetime import datetime

# Create your models here.
class Producto(models.Model):
    código_producto = models.CharField(max_length=100, primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    cantidad_productos = models.IntegerField()
    fecha = models.DateField(default=datetime.now)
    productos_ok = models.BooleanField(default=True)
    cantidad_productos_ok = models.IntegerField(default=0)
    merma = models.IntegerField(default=0)
    precio_compra = models.IntegerField()
    total_compra = models.IntegerField()
    inversion_ok = models.BooleanField(default=True)
    perdida = models.IntegerField(default=0)
    precio_unitario = models.IntegerField()
    nombre_local = models.CharField(max_length=100)
    dirección_local = models.CharField(max_length=100)
