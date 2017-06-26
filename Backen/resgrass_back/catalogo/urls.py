from django.conf.urls import url, include
from rest_framework import routers
from catalogo.views.empresa import EmpresaViewSet
from catalogo.views.local import LocalViewSet
from catalogo.views.tipo_cancha import TipoCanchaViewSet
from catalogo.views.archivo import ArchivoViewSet
from catalogo.views.cancha import CanchaViewSet,CanchaGetViewSet
from catalogo.views.catalogo import CatalogoViewSet
from catalogo.views.implementos_dep import ImplementoViewSet
from catalogo.views.persona import PersonaViewSet
router = routers.DefaultRouter()
router.register(r'tipo-cancha', TipoCanchaViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'local', LocalViewSet)
router.register(r'archivo', ArchivoViewSet)
router.register(r'cancha', CanchaViewSet)
router.register(r'catalogo', CatalogoViewSet)
router.register(r'Implemento', ImplementoViewSet)
router.register(r'persona', PersonaViewSet)
router.register(r'cancha-get', CanchaGetViewSet)
urlpatterns = [

    url(r'^', include(router.urls)),




]
