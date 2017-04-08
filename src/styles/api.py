from rest_framework import viewsets, permissions

from .models import Style
from .serializers import StyleSerializer


class StyleViewSet(viewsets.ModelViewSet):
    serializer_class = StyleSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Style.objects.all()
