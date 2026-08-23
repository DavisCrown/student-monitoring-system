from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer
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

ALLOWED_TO_CREATE = {
    'admin': 'dean',
    'dean': 'hod'
}
class RegisterUserView(APIView):
    def post(self,request):
        permission_classes = [IsAuthenticated]
        requester_role = request.user.role
        target_role = request.data.get('role')

        if ALLOWED_TO_CREATE.get(requester_role) != target_role:
            return Response({'detail':"You're not allowed to create this role"}, status=status.HTTP_403_FORBIDDEN)

        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'user': UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)