from django.db import models
from django.utils.translation import ugettext_lazy as _

from pubs.models import Pub
from beers.models import Beer

class PubVisit(models.Model):
    pub = models.ForeignKey(Pub, related_name='pubvisits', verbose_name=_('pub'))
    beer = models.ManyToManyField(Beer, verbose_name=_('beer'))
    date = models.DateField(verbose_name=_('date'), auto_now_add=True)

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = _('Pub visit')
        verbose_name_plural = _('Pub visits')