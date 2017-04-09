from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers


import pubs.api
import events.api
import beers.api
import breweries.api
import styles.api

router = routers.DefaultRouter()

# pubs
router.register(
    'pubs', pubs.api.PubViewSet, 'pubs',
)
# events
router.register(
    'events', events.api.EventViewSet, 'events',
)
# beers
router.register(
    'beers', beers.api.BeerViewSet, 'beers',
    
)
router.register(
    'reviews', beers.api.BeerReviewViewSet, 'reviews',
)
router.register(
    'breweries', breweries.api.BreweryViewSet, 'breweries',
)
router.register(
    'styles', styles.api.StyleViewSet, 'styles',
)
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
