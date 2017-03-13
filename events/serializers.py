from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    place = serializers.HyperlinkedIdentityField()
    class Meta:
        model = Event
        fields = ('name', 'start_date', 'end_date', 'description',)