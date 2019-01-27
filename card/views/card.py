from rest_framework import viewsets as views
from card import models
from rest_framework import permissions
from card.serializers import card


class CardViewSet(views.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.Card.objects.filter(is_deleted=False)
    serializer_class = card.CardSerializer
