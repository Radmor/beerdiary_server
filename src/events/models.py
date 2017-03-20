from django.db import models
from django.utils.translation import ugettext_lazy as _
from pubs.models import Pub


class Event(models.Model):
    name = models.CharField(_('name'), max_length=256)
    start_date = models.DateTimeField(_('start date'))
    end_date = models.DateTimeField(_('end date'), blank=True, null=True)
    description = models.TextField(_('description'), blank=True)
    place = models.ForeignKey(Pub, related_name='events')

    def __str__(self):
        return "{} {}".format(self.name, self.start_date)

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
