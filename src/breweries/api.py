from rest_framework import viewsets, permissions
from rest_framework import pagination

from .models import Brewery
from .serializers import BrewerySerializer

class CustomPagination(pagination.PageNumberPagination):
    page_size = 2

class BreweryViewSet(viewsets.ModelViewSet):
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Brewery.objects.all()
    pagination_class = CustomPagination