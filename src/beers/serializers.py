from rest_framework import serializers

from .models import Beer, BeerReview


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ('name', 'brewery', 'style', 'overall', 'premiere_date', 'note')


class BeerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerReview
        fields = ('beer', 'created', 'overall', 'bitterness',
                  'bitterness_description', 'foam', 'foam_description', 'ibu',
                  'color', 'aroma', 'aroma_description', 'taste', 'taste_description',
                  'palate', 'palate_description')
