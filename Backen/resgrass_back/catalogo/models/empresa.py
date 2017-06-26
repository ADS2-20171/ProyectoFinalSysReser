from uuid import uuid4
from django.db import models


class Empresa(models.Model):


    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    razon_social = models.CharField(max_length=100)
    ruc = models.IntegerField()
    logo = models.ImageField(verbose_name='Imagen', null=True, upload_to='images/')
    descripcion = models.TextField()
    direccion =models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    email = models.EmailField()


    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"


    def __str__(self):
        return self.razon_social
