from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import( 
    SpectacularAPIView, 
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from users.router import router_users
from catalogos.router import (
    router_parentesco,
    router_puesto
)
from empleados.router import router_empleado
from beneficiarios.router import router_beneficiario

urlpatterns = [
    path('admin/', admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/",SpectacularSwaggerView.as_view( url_name="schema"),
        name="swagger-ui",
    ),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', include('users.router')),
    path("api/", include(router_users.urls)),
    path("api/", include(router_parentesco.urls)),
    path("api/", include(router_puesto.urls)),
    path("api/", include(router_empleado.urls)),
    path("api/", include(router_beneficiario.urls)),
]
