from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from rest_framework.views import APIView
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"})
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer