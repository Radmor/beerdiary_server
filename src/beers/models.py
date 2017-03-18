from django.db import models
from django.utils.translation import ugettext as _

from beerdiary_server.fields import RatingField, SliderField
from breweries.models import Brewery
from styles.models import Style

class Beer(models.Model):
    name = models.CharField(_('name'), max_length=256)
    brewery = models.ForeignKey(Brewery, related_name='beers')
    style = models.ForeignKey(Style, related_name='beers')
    overall = models.FloatField(_('overall'))

    # advanced
    premiere_date = models.DateField(_('premiere date'), blank=True, null=True)
    note = models.TextField(_('note'), blank=True, null=True)

    def __str__(self):
        return '{}, {}'.format(self.name, self.brewery.name)

    class Meta:
        verbose_name = _('beer')
        verbose_name_plural = _('beers')


class BeerReview(models.Model):
    beer = models.ForeignKey(Beer, related_name='reviews')
    created = models.DateTimeField(_('created'), auto_now_add=True)
    overall = RatingField(_('overall'))
    bitterness = SliderField(_('bitterness'), blank=True, null=True)
    bitterness_description = models.CharField(_('bitterness description'),
                                              max_length=256, blank=True,
                                              null=True)
    foam = SliderField(_('foam'), blank=True, null=True)
    foam_description = models.CharField(_('foam description'), max_length=256,
                                        blank=True, null=True)
    ibu = models.PositiveIntegerField(_('ibu'), blank=True, null=True)
    color = models.CharField(_('color'), max_length=256, blank=True, null=True)
    aroma = SliderField(_('aroma'), blank=True, null=True)
    aroma_description = models.CharField(_('aroma description'), max_length=256,
                                         blank=True, null=True)
    taste = SliderField(_('taste'), blank=True, null=True)
    taste_description = models.CharField(_('taste description'), max_length=256,
                                         blank=True, null=True)
    palate = SliderField(_('palate'), blank=True, null=True)
    palate_description = models.CharField(_('palate description'),
                                          max_length=256, blank=True, null=True)

    def __str__(self):
        return '{}, {}'.format(self.beer, self.created)

    class Meta:
        verbose_name = _('beer review')
        verbose_name_plural = _('beer reviews')
        ordering = ('beer', 'created')
