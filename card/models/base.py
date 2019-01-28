from django.db import models
from datetime import datetime


class BaseModel(models.Model):
    created = models.DateTimeField(default=datetime.now, blank=True)
    changed = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
