from rest_framework.serializers import ModelSerializer

from users.models import Users

class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"