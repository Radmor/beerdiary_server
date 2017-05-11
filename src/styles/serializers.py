from rest_framework import serializers

from .models import Style


class StyleSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Style
        fields = ('id', 'name',)
        