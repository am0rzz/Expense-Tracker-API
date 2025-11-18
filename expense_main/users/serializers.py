from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','date_of_birth','password']
        read_only_fields = ['is_staff','is_superuser','is_active']

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


