from rest_framework import viewsets, permissions

from .models import PubVisit
from .serializers import PubVisitSerializer

class PubVisitViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = PubVisit.objects.all()
    serializer_class = PubVisitSerializer