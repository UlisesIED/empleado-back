from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
import base64
import imghdr

from empleados.models import Empleados
from users.models import Users
from catalogos.models import Puesto
from empleados.serializers import EmpleadosSerializer, ViewEmpleadosSerializer

class EmpleadosApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ViewEmpleadosSerializer
    queryset = Empleados.objects.all()

    @action(
        detail=False,
        methods=['post'],
        url_path='agregarEmpleado'
    )
    def agregarEmpleado(self, request):
        password = make_password(request.data['password'])
        image64 = None
        try:
            imagen = request.data.get('fotografia', None)
            if imagen:
                file_content = request.data['fotografia'].read()
                base64_string = base64.b64encode(file_content).decode('utf-8')
                image_type = imghdr.what(None, h=file_content)
                image64 = f"data:image/{image_type};base64,{base64_string}"
        except Exception as e:
            print("Error en la generación de imagen en Base64")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            usuario = Users(
            username = request.data['username'],
            password = password,
            role = 2,
            )
            usuario.save()
        except Exception as e:
            print(f"Error en la generación del usuario\n{e}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            puesto = Puesto.objects.get(id = request.data['puesto'])
            empleado = Empleados(
                user = usuario,
                fecha_nacimiento = request.data['fecha_nacimiento'],
                fotografia = image64 if image64 else None ,
                puesto = puesto,
                salario = request.data['salario'],
                nombre = request.data['nombre'],
                a_paterno = request.data['a_paterno'],            
                a_materno = request.data.get('a_materno', None),
            )
            empleado.save()
            print(f"Empleado creado con éxito con id: {empleado.id}")
            return Response(empleado.id, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error en la generación del Empleado\n{e}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    @action(
        detail=False,
        methods=['patch'],
        url_path='editarEmpleado'
    )
    def editarEmpleado(self, request):
        print(request.data)
        password = request.data.get('password', None)
        empleado = Empleados.objects.get(id = request.data['id'])
        image64 = None
        try:
            imagen = request.data.get('fotografia', None)
            if imagen:
                request.data._mutable = True
                file_content = request.data['fotografia'].read()
                base64_string = base64.b64encode(file_content).decode('utf-8')
                image_type = imghdr.what(None, h=file_content)
                image64 = f"data:image/{image_type};base64,{base64_string}"
                print("imagen")
                request.data["fotografia"] = image64
        except Exception as e:
            print("Error en la generación de imagen en Base64")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            if password: 
                usuario = Users.objects.get(id = empleado.user.id)
                usuario.password = make_password(password)
                usuario.save()    
                print("Usuario actualizado con éxito")
        except Exception as e:
            print(f"Error en la actualizacion del usuario\n{e}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            for key, value in request.data.items():
                if hasattr(empleado, key):
                    if key == "puesto":
                        value = Puesto.objects.get(id = request.data['puesto'])
                    print(key, value)
                    setattr(empleado, key, value)
            empleado.save()
            print("empleado actualizado con éxito")
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error en la actualizacion del empleado\n{e}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        