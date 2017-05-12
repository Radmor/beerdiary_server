from django.utils.translation import ugettext as _

from rest_framework import serializers

from .models import Event
from pubs.models import Pub
from pubs.serializers import PubSerializer


class EventSerializer(serializers.ModelSerializer):
    place = serializers.PrimaryKeyRelatedField(queryset=Pub.objects.all())

    def validate(self, data):
        if data.get('start_date') > data.get('end_date'):
            raise serializers.ValidationError({'end_date': _('End date must occur after start date')})
        return data

    class Meta:
        model = Event
        fields = ('name', 'start_date', 'end_date', 'description', 'place')
