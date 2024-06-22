from rest_framework.routers import DefaultRouter

from beneficiarios.views import BeneficiariosApiViewSet

router_beneficiario = DefaultRouter()
router_beneficiario.register(
    prefix="beneficiarios",
    basename="beneficiarios",
    viewset=BeneficiariosApiViewSet,
)
