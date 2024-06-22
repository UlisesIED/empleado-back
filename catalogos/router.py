from rest_framework.routers import DefaultRouter

from catalogos.views import (
    ParentescoApiViewSet,
    PuestoApiViewSet
)

router_parentesco = DefaultRouter()
router_parentesco.register(
    prefix="parentesco",
    basename="parentesco",
    viewset=ParentescoApiViewSet
)

router_puesto = DefaultRouter()
router_puesto.register(
    prefix="puesto",
    basename="puesto",
    viewset=PuestoApiViewSet
)