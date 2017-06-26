from rest_framework import serializers, viewsets

from catalogo.models.tipo_cancha import TipoCancha

import logging

log = logging.getLogger(__name__)




class TipoCanchaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoCancha
        fields = '__all__'


class TipoCanchaViewSet(viewsets.ModelViewSet):
    queryset = TipoCancha.objects.all()
    serializer_class = TipoCanchaSerializer
