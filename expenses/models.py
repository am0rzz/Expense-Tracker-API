from django.db import models

# Create your models here.


class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category_choices = {
        "GR" : "Groceries",
        "LE" : "Leisure",
        "EL" : "Electronics",
        "UT" : "Utilities",
        "CL" : "Clothing",
        "HE" : "Health",
        "OT" : "Others"
    }
    categories = ['Groceries', 'Leisure', 'Electronics', 'Utilities', 'Clothing', 'Health', 'Others']
    category = models.CharField(max_length=2, choices=category_choices, default="OT")