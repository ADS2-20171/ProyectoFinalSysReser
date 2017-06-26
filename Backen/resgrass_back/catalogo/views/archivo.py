from rest_framework import serializers, viewsets

from catalogo.models.archivo import Archivo

import logging

log = logging.getLogger(__name__)



class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields = '__all__'


class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer