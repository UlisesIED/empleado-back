from rest_framework.routers import DefaultRouter

from empleados.views import EmpleadosApiViewSet

router_empleado = DefaultRouter()
router_empleado.register(
    viewset=EmpleadosApiViewSet,
    basename="empleados",
    prefix="empleados"
)
