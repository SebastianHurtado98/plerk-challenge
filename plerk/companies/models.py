from django.db import models
from django.utils.translation import gettext_lazy as _

from .choices import STATUS_CHOICES

import uuid

class Company(models.Model):
    name = models.CharField(_('name'), max_length=200)
    status = models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')
        ordering = ['name']

    def __str__(self):
        return self.name