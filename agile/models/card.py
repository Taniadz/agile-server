from .base import BaseModel
from django.db import models
from django.contrib.auth.models import User

STATUS_TYPES = ("TO DO", 'IN PROGRESS', "DONE")


class Card(BaseModel):
    time_to = models.DateTimeField(null=True)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subsribed = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="card_subsribed", null=True)
    status = models.CharField(choices=tuple(map(lambda x: (x, x), STATUS_TYPES)),max_length=10)
