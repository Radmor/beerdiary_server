from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.utils.translation import ugettext as _

from beerdiary_server.fields import RatingField, SliderField


class Pub(models. Model):
    name = models.CharField(_('name'), max_length=256)
    street = models.CharField(_('street'), max_length=256, blank=True)
    city = models.CharField(_('city'), max_length=64, blank=True)

    overall = RatingField(_('overall'))
    design = SliderField(_('design'), blank=True, null=True)
    design_description = models.TextField(_('design description'), blank=True)
    atmosphere = SliderField(_('atmosphere'), blank=True, null=True)
    atmosphere_description = models.TextField(_('atmosphere description'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('pub')
        verbose_name_plural = _('pubs')
