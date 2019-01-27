from rest_framework import viewsets
from django.contrib.auth.models import User

from card.serializers import user


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user.UserSerializer
