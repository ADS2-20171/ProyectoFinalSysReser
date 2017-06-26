from uuid import uuid4
from django.db import models

from catalogo.models.cancha import Cancha

class Archivo(models.Model):


    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(verbose_name='Imagen', null=True, upload_to='images/')
    cancha = models.ForeignKey(Cancha)


    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"


    def __str__(self):
        return self.nombre
