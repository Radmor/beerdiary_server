from rest_framework import viewsets, permissions
from .models import Pub
from .serializers import PubSerializer


class PubViewSet(viewsets.ModelViewSet):
    serializer_class = PubSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        current_user = self.request.user
        return Pub.objects.all()