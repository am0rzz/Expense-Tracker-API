from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    description = serializers.CharField(allow_blank=True)
    class Meta:
        model = Expense
        fields = '__all__'