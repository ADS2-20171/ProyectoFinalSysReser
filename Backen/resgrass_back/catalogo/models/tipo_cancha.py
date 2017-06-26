from uuid import uuid4
from django.db import models


class TipoCancha(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "TipoCancha"

        verbose_name_plural = "TipoCanchas"


    def __str__(self):
        return self.nombre
