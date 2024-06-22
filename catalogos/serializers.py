from rest_framework.serializers import ModelSerializer

from catalogos.models import (
    Parentesco,
    Puesto,
)

class PuestoSerializer(ModelSerializer):
    class Meta:
        model = Puesto
        fields = "__all__"
        

class ParentescoSerializer(ModelSerializer):
    class Meta:
        model = Parentesco
        fields = "__all__"
        
