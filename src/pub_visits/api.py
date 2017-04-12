from rest_framework import viewsets, permissions

from .models import PubVisit
from .serializers import PubVisitSerializer, PubVisitBeersNestedSerializer
from beers.models import Beer
from pubs.models import Pub
from breweries.models import Brewery
from styles.models import Style

class PubVisitViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = PubVisit.objects.all()
    serializer_class = PubVisitSerializer


class PubVisitBeerNestedViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = PubVisit.objects.all()
    serializer_class = PubVisitBeersNestedSerializer

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        beers_data = validated_data.data.pop('beers')
        pub = Pub.objects.get(id=validated_data.data.get('pub'))
        pub_visit = PubVisit.objects.create(pub = pub, date=validated_data.data.pop('date'))

        for beer in beers_data:
            beer['brewery'] = Brewery.objects.get(id=beer['brewery'])
            beer['style'] = Style.objects.get(id=beer['style'])
            beer_object = Beer.objects.create(**beer)
            pub_visit.beers.add(beer_object)
            
        return pub_visit
