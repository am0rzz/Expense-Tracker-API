from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import SignupSerializer

# Create your views here.

class Register(APIView):
    def post(self,request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'message': 'Register Failed!'}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        """
        USED ONLY DURING PRODUCTION!
        """
        queryset = User.objects.all()
        serializer = SignupSerializer(queryset,many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Couldn\'t Retrieve Users}'}, status=status.HTTP_400_BAD_REQUEST)
    
