from rest_framework import serializers, viewsets

from catalogo.models.empresa import Empresa

import logging

log = logging.getLogger(__name__)



class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

