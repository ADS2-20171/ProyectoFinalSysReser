from uuid import uuid4
from django.db import models
from catalogo.models.empresa import Empresa
class Local(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    nombre_local=models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    numero_telefono = models.IntegerField(max_length=12)
    empresa = models.ForeignKey(Empresa, blank=True,null=True)
    estado=models.BooleanField(default=True)
    email = models.EmailField()

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locals"

    def __str__(self):
        return self.nombre_local