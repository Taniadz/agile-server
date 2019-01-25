from rest_framework import viewsets as views
from agile import models
from agile import serializers


class CardViewSet(views.ModelViewSet):
    queryset = models.Card.objects.filter(is_deleted=False)
    serializer_class = serializers.card.CardSerializer
