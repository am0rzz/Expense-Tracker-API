from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import SignupSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class Register(APIView):
    def post(self,request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            data = serializer.data
            data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
            return Response(data,status=status.HTTP_201_CREATED)
        return Response({'message': 'Register Failed!'}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        """
        USED ONLY DURING PRODUCTION!
        """
        queryset = User.objects.all()
        serializer = SignupSerializer(queryset,many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Couldn\'t Retrieve Users'}, status=status.HTTP_400_BAD_REQUEST)
    
class LogOutView(APIView): 
    permission_classes = [permissions.IsAuthenticated] 
    authentication_classes = [JWTAuthentication] 

    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response({'message': 'Logged out sucssesfully!'}, status=status.HTTP_205_RESET_CONTENT)

