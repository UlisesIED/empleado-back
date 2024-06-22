from rest_framework.serializers import ModelSerializer

from empleados.models import Empleados
from catalogos.serializers import PuestoSerializer
from users.serializers import UsersSerializer

class EmpleadosSerializer(ModelSerializer):
    
    class Meta:
        model = Empleados
        fields = "__all__"
        
class ViewEmpleadosSerializer(ModelSerializer):
    puesto = PuestoSerializer(read_only = True)
    user  = UsersSerializer(read_only = True)
    class Meta:
        model = Empleados
        fields = "__all__"