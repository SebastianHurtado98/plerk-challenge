from rest_framework import serializers
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK

from django.db.models import F, Count, Sum, Q
from django.shortcuts import get_object_or_404


from ..models import (
    Company,
)
from .serializers import (
    CompanySummarySerializer,
    CompanyTestingSerializer,
)

from plerk.transactions.models import (
    Transaction,
)

class CompanyBaseViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        GenericViewSet):
    pass

class CompanyViewSet(CompanyBaseViewSet):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CompanyTestingSerializer
        if self.action == 'retrieve':
            return CompanySummarySerializer

    @action(detail=False, methods=["get"])
    def summary(self, request):
        companies_by_transactions = Transaction.objects.exclude(company=None).values('company').annotate(
            name=F('company__name'), total=Count('company'))
        top_company = companies_by_transactions.order_by('-total').first()["name"]
        bottom_company = companies_by_transactions.order_by('total').first()["name"]
        complete_transactions = Transaction.objects.exclude(company=None).filter(status_transaction=1, status_approved=True)
        uncomplete_transactions = Transaction.objects.exclude(company=None).exclude(status_transaction=1, status_approved=True)
        total_price_complete_transactions = complete_transactions.aggregate(total_price=Sum('price'))["total_price"]
        total_price_uncomplete_transactions = uncomplete_transactions.aggregate(total_price=Sum('price'))["total_price"]
        top_rejections_company = uncomplete_transactions.values('company').annotate(
            name=F('company__name'), total=Count('company')).order_by('-total').first()["name"]
        response = {
            'top_sales_company': top_company,
            'bottom_sales_company': bottom_company,
            'total_price_complete_transactions': total_price_complete_transactions,
            'total_price_uncomplete_transactions': total_price_uncomplete_transactions,
            'top_rejections_company': top_rejections_company
        }
        return Response(response, status=HTTP_200_OK)