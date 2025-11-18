from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import ExpenseSerializer
from rest_framework.response import Response
from rest_framework import serializers
from .models import Expense
from rest_framework import status
# Create your views here.


class ExpenseViewSet(viewsets.ViewSet):

    def list(self,request):
        """
        Retrieve all models using a GET request.
        """
        queryset = Expense.objects.all()
        serializer = ExpenseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        """
        Retrieve an existing model using a GET request.
        """
        queryset = Expense.objects.all()
        try:
            expense = get_object_or_404(queryset, pk=pk)
        except:
            return Response({'message': 'Object is not Available.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        """
        Create a new Model using a PUT request
        """
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        """
        Update exisiting Model using a PUT request
        """
        queryset = Expense.objects.all()
        try:
            expense = get_object_or_404(queryset, pk=pk)
        except:
            return Response({'message': 'Object is not Available.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ExpenseSerializer(expense,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        """
        Update exisiting Model using a PATCH request
        """
        queryset = Expense.objects.all()
        expense = get_object_or_404(queryset, pk=pk)
        serializer = ExpenseSerializer(expense,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        """
        Delete an existing Model using a DELETE request
        """
        queryset = Expense.objects.all()
        try:
            expense = get_object_or_404(queryset, pk=pk)
        except:
            return Response({'message': 'Object is not Available.'}, status=status.HTTP_400_BAD_REQUEST)
        if expense.delete():
            return Response({'message': 'Deleted Sucssesfully!'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Couldn\'t Delete.'}, status=status.HTTP_400_BAD_REQUEST)