from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(default=datetime.now, blank=True,
                                   verbose_name=_('created'))
    changed = models.DateTimeField(auto_now=True, verbose_name=_('changed'))
    is_deleted = models.BooleanField(default=False,
                                     verbose_name=_('is deleted'))

    class Meta:
        abstract = True
