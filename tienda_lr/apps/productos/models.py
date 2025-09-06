from django.db import models
from cloudinary.models import CloudinaryField

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.PositiveIntegerField(default=0)
    imagen = CloudinaryField('imagen', blank=True, null=True)

    def __str__(self):
        return self.nombre

# Create your models here.
