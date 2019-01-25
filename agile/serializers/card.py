from rest_framework import serializers
from agile import models
from django.contrib.auth.models import User


class CardUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class CardSerializer(serializers.ModelSerializer):
    subsribed = CardUserSerializer(read_only=True)
    subsribed_id = serializers.IntegerField(write_only=True, required=False)
    author_id = serializers.IntegerField(write_only=True)
    author = CardUserSerializer(read_only=True)

    class Meta:
        model = models.Card
        fields = ("subsribed", "author", "subsribed_id", "author_id",
                  "title", "description", "status", "time_to", "id", "is_deleted")
        read_only_fields = ("id",)

