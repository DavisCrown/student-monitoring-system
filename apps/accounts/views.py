from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, LoginSerializer
from rest_framework.views import APIView

# Create your views here.
class LoginView(APIView):
    permission_classes =[AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': UserSerializer(user).data},
            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)