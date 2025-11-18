from django.db import models
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_superuser",True)
        user = self.create_user(
            email = email,
            password = password,
            **extra_fields
        )

        user.save()
        return user