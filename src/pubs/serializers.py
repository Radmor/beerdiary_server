from rest_framework import serializers
from .models import Pub


class PubSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Pub
        fields = ('id', 'name', 'street', 'city', 'overall', 'design', 'design_description', 'atmosphere', 'atmosphere_description',)
