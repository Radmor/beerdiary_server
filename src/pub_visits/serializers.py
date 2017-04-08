from rest_framework import serializers
from .models import PubVisit


class PubVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PubVisit
        fields = ('date', 'beer', 'pub',)
