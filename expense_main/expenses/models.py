from datetime import date

from django.db import models
from django.core.validators import MinValueValidator 
from decimal import Decimal
from django.conf import settings
# Create your models here.


class Expense(models.Model):
    title = models.CharField(max_length=100, blank= False)
    amount = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(Decimal('0.01'))], blank=False)
    description = models.TextField(blank=True)
    category_choices = {
        "GR" : "Groceries",
        "LE" : "Leisure",
        "EL" : "Electronics",
        "UT" : "Utilities",
        "CL" : "Clothing",
        "HE" : "Health",
        "OT" : "Others"
    }
    category = models.CharField(max_length=2, choices=category_choices, default="OT")
    date_added = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
   
####### Categories with its own entity ########