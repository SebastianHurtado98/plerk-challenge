from django_filters import FilterSet, AllValuesFilter, DateTimeFilter, NumberFilter

from ..models import (
    Transaction,
)

class TransactionFilter(FilterSet):
    from_date = DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    to_date = DateTimeFilter(field_name='timestamp', lookup_expr='lte')
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    status_transaction = AllValuesFilter(field_name='status_transaction')
    status_approved = AllValuesFilter(field_name='status_approved')
    company = AllValuesFilter(field_name='company__name')
  
    class Meta:
        model = Transaction
        fields = (
            'from_date',
            'to_date',
            'min_price',
            'max_price',
            'status_transaction',
            'status_approved',
            'company',
        )