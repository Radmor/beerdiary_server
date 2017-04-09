from rest_framework import serializers
from .models import PubVisit

from beers.serializers import BeerSerializer

class PubVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PubVisit
        fields = ('date', 'beers', 'pub',)


class PubVisitBeersNestedSerializer(serializers.ModelSerializer):
    beers = BeerSerializer(many=True)

    class Meta:
        model = PubVisit
        fields = ('date', 'beers', 'pub')