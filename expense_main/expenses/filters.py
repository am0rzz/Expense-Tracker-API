from datetime import date, timedelta

import django_filters
from .models import Expense


class ExpenseFilter(django_filters.FilterSet):
    created_after = django_filters.DateFilter(field_name='date_added', lookup_expr='gt')
    created_at = django_filters.DateFilter(field_name='date_added', lookup_expr='exact')
    created_before = django_filters.DateFilter(field_name='date_added', lookup_expr='lt')
    period = django_filters.CharFilter(method = 'filter_method')

    class Meta:
        model = Expense
        fields = ['created_after', 'created_before', 'period','created_at']

    def filter_method(self,queryset,name,value):
        
        if value == 'past_week':
            start = date.today()
            end = date.today() - timedelta(days=7)
        
        elif value == 'past_month':
            today = date.today()
            first = today.replace(day=1)
            end = first - timedelta(days=1)
            start = (first - timedelta(days=1)).replace(day=1)

        elif value == 'past_year':
            today = date.today()
            start = today.replace(day=1,month=1,year=(date.today().year)-1)
            end = today.replace(day=31,month=12,year=(date.today().year)-1)
        
        else:
            return queryset

        return queryset.filter(date_added__range=(start, end))

            