from rest_framework import viewsets, permissions

from .serializers import BeerSerializer, BeerReviewSerializer
from .models import Beer, BeerReview


class BeerViewSet(viewsets.ModelViewSet):
    serializer_class = BeerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Beer.objects.all()


class BeerReviewViewSet(viewsets.ModelViewSet):
    serializer_class = BeerReviewSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BeerReview.objects.all()
    