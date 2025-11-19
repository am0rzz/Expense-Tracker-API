from django.contrib import admin
from .models import Expense
# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'amount',
        'owner',
        'date_added'
    ]
    list_filter = ['category']


admin.site.register(Expense,ExpenseAdmin)
