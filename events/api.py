from rest_framework import viewsets, permissions

from .serializers import EventSerializer
from .models import Event

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Event.objects.all()