from rest_framework import viewsets, permissions

from .models import Brewery
from .serializers import BrewerySerializer

class BreweryViewSet(viewsets.ModelViewSet):
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Brewery.objects.all()