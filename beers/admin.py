from django.contrib import admin

from .models import Beer, BeerReview

@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'brewery')


@admin.register(BeerReview)
class BeerReviewAdmin(admin.ModelAdmin):
    list_display = ('beer', 'created')