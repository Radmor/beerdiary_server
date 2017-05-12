from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from .views import FacebookLogin, GoogleLogin

import pubs.api
import events.api
import beers.api
import breweries.api
import styles.api
import pub_visits.api

router = routers.DefaultRouter(trailing_slash=False)

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
router.register(
    'pub_visits', pub_visits.api.PubVisitViewSet, 'pub_visits'
)
router.register(
    'pub_visits_beer_nested', pub_visits.api.PubVisitBeerNestedViewSet, 'pub_visits_beer_nested'
)
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),
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
