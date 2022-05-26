from django.db import models
from django.utils.translation import gettext_lazy as _

from plerk.transactions.choices import STATUS_CHOICES

from plerk.companies.models import Company

import uuid

# Create your models here.

class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name=_('company'))
    price = models.PositiveIntegerField(_('price'))
    timestamp = models.DateTimeField(_('timestamp'))
    status_transaction = models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES)
    status_approved = models.BooleanField(_('approved status'))
    
    class Meta:
        verbose_name = _('transaction')
        verbose_name_plural = _('transactions')
        ordering = ['timestamp']

    def __str__(self):
        return self.company.name + '-' + str(self.id)

    @property
    def payment(self):
        return status_transaction == 1 and status_approved