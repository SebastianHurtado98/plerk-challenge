from rest_framework import serializers

from ..models import (
    Transaction,
)

from plerk.companies.api.serializers import CompanySerializer

class TransactionSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    class Meta:
        model = Transaction
        fields = [
            "company",
            "price",
            "timestamp",
            "status_transaction",
            "status_approved",
        ]