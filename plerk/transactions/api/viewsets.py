
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from ..models import (
    Transaction,
)
from .serializers import (
    TransactionSerializer,
)
from .filters import (
    TransactionFilter,
)

class TransactionBaseViewSet(
        mixins.ListModelMixin,
        GenericViewSet):
    pass

class TransactionViewSet(TransactionBaseViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_class = TransactionFilter