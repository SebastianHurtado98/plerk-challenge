from rest_framework import serializers
from django.db.models import F, Count, Func, Value, CharField

from plerk.transactions.models import Transaction

from ..models import (
    Company,
)
# No queremos ejecutar queries pesados en un llamado general
class CompanySummarySerializer(serializers.ModelSerializer):
    complete_transactions = serializers.SerializerMethodField()
    uncomplete_transactions = serializers.SerializerMethodField()
    peak_day_transactions = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = [
            "name",
            "complete_transactions",
            "uncomplete_transactions",
            "peak_day_transactions",
        ]

    def get_complete_transactions(self, obj):
        return Transaction.objects.filter(company=obj, status_transaction=1, status_approved=True).count()
    
    def get_uncomplete_transactions(self, obj):
        return Transaction.objects.filter(company=obj).exclude(status_transaction=1, status_approved=True).count()
    
    def get_peak_day_transactions(self, obj):
        return Transaction.objects.filter(company=obj).values('timestamp').annotate(
                day=Func(
                    F('timestamp'),
                    Value('YYYY-MM-DD'),
                    function='to_char',
                    output_field=CharField(),
                total=Count('day'))
            ).first()['day']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "name",
            "status",
        ]

# Este serializer lo creo para propósitos de testing.
# El id no debería ser público para evitar que obtengan la data tan fácil.
class CompanyTestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'