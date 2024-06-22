from django.db import models
from django.utils import timezone
from uuid import uuid4

from catalogos.models import Puesto
from users.models import Persona, Users

class Empleados(Persona):
    
    ACTIVO = 1
    DE_BAJA = 2
    ENFERMO = 3
    VACACIONES = 4
    
    STATUS_CHOICES = (
        (ACTIVO, "Activo"),
        (DE_BAJA, "De baja"),
        (ENFERMO, "Enfermo"),
        (VACACIONES, "Vacaciones"),
    )
    
    id = models.UUIDField(
        default=uuid4, 
        unique=True, 
        editable=False, 
        primary_key=True
    )
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField(
        editable=False, 
        auto_now_add=True, 
    )
    fotografia = models.TextField(null=True, blank=True)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    salario = models.FloatField(null=False)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)
    
    
    @property
    def edad(self):
        hoy = timezone.now().date()
        edad = int(
            hoy.year 
            - self.fecha_nacimiento.year
            - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        )
        return edad
 