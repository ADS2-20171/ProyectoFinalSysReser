from rest_framework import serializers, viewsets

from catalogo.models.cancha import Cancha

import logging

log = logging.getLogger(__name__)



class CanchaSerializer(serializers.ModelSerializer):
    #tipo_cancha = serializers.SlugRelatedField(read_only=True, slug_field='nombre', )
    class Meta:
        model = Cancha
        fields = '__all__'


class CanchaGetSerializer(serializers.ModelSerializer):
    tipo_cancha = serializers.SlugRelatedField(read_only=True, slug_field='nombre', )
    class Meta:
        model = Cancha
        fields = '__all__'


class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer

class CanchaGetViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaGetSerializer