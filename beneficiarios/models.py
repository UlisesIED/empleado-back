from django.db import models
from uuid import uuid4

from catalogos.models import Parentesco
from empleados.models import Empleados, Persona

class Beneficiarios(Persona):
    id = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        primary_key=True
    )
    empleado = models.ForeignKey(
        Empleados,
        on_delete=models.CASCADE
    )
    parentesco = models.ForeignKey(
        Parentesco,
        on_delete=models.CASCADE
    )