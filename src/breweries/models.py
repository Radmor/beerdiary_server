from django.db import models

from django.utils.translation import ugettext as _

from beerdiary_server.fields import RatingField

class Brewery(models.Model):
    name = models.CharField(_('name'), max_length=256, unique=True)
    overall = RatingField(_('overall'), blank=True, null=True)
    note = models.TextField(_('note'), blank=True)

    class Meta:
        verbose_name = _('brewery')
        verbose_name_plural = _('breweries')
        