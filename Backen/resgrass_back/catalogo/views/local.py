from rest_framework import serializers, viewsets

from catalogo.models.local import Local

import logging

log = logging.getLogger(__name__)




class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'


class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

