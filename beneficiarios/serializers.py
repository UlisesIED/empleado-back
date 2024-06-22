from rest_framework.serializers import ModelSerializer

from beneficiarios.models import Beneficiarios

class BeneficiariosSerializer(ModelSerializer):
    class Meta:
        model = Beneficiarios
        fields = "__all__"