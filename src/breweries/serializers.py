from rest_framework import serializers

from .models import Brewery


class BrewerySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Brewery
        fields = ('id', 'name', 'overall', 'note')