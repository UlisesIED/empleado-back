from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Users
from users.serializers import UsersSerializer

User = get_user_model()

class UsersApiViewSet(ModelViewSet):
    permission_classes = [ IsAdminUser ]
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        print(request.user)
        serializer=UsersSerializer(request.user)
        return Response(serializer.data)
    
    