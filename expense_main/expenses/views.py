from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import ExpenseSerializer
from rest_framework.response import Response
from .models import Expense
from rest_framework import status
from .filters import ExpenseFilter
from django_filters import rest_framework as filters

# Create your views here.


class ExpenseViewSet(viewsets.ViewSet):

    def list(self,request):
        """
        Retrieve all models using a GET request.
        """
        try:
            queryset = Expense.objects.filter(owner=self.request.user)
            f = ExpenseFilter(request.GET, queryset=queryset)
            qs = f.qs
            serializer = ExpenseSerializer(qs, many=True)
        except:
            return Response({'message': 'You must be logged in!'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        """
        Retrieve an existing model using a GET request.
        """
        queryset = Expense.objects.filter(owner=self.request.user)
        try:
            expense = get_object_or_404(queryset, pk=pk)
        except:
            return Response({'message': 'Object is not Available.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        """
        Create a new Model using a POST request
        """
        request.data["owner"] = self.request.user.id
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        """
        Update exisiting Model using a PUT request
        """
        queryset = Expense.objects.filter(owner=self.request.user)
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
        queryset = Expense.objects.filter(owner=self.request.user)
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
        queryset = Expense.objects.filter(owner=self.request.user)
        try:
            expense = get_object_or_404(queryset, pk=pk)
        except:
            return Response({'message': 'Object is not Available.'}, status=status.HTTP_400_BAD_REQUEST)
        if expense.delete():
            return Response({'message': 'Deleted Sucssesfully!'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Couldn\'t Delete.'}, status=status.HTTP_400_BAD_REQUEST)