from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
import json

from back_empleados.metodosGlobales import hacerConsultaSQL
from beneficiarios.models import Beneficiarios
from beneficiarios.serializers import BeneficiariosSerializer

class BeneficiariosApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = BeneficiariosSerializer
    queryset = Beneficiarios.objects.all()
    
    @action(
        detail=False,
        methods=['get'],
        url_path=r'obtenerBeneficiarios'
    )
    def obtenerBeneficiarios(self, request):
        print("ola papu")
        idEmpleado = json.loads(request.query_params.get("idEmpleado"))
        print(idEmpleado)
        consulta = f"""
        select b.id, b.nombre, b.a_paterno, b.a_materno, p.descripcion from beneficiarios_beneficiarios b
        inner join catalogos_parentesco p on b.parentesco_id = p.id 
        where b.empleado_id = '{idEmpleado}'
        """
        respuesta = hacerConsultaSQL(consulta=consulta)
        return Response(respuesta, status=status.HTTP_200_OK)
        
    