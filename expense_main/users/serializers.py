from rest_framework import serializers
from .models import User

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','date_of_birth']
        read_only_fields = ['is_staff','is_superuser','is_active']