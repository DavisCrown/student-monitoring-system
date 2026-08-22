from .models import User
from rest_framework import serializers 
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class LoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self, attrs):
        login = attrs.get('login')
        password = attrs.get('password')

        user = User.objects.filter(username=login).first() or User.objects.filter(email=login).first()
        if not user:
            raise serializers.ValidationError('Invalid Login Credentials')
        
        authenticated_user = authenticate(username=user.username, password=password)
        if not authenticated_user:
            raise serializers.ValidationError('Invalid credentials')
        attrs['user'] = authenticated_user
        return attrs