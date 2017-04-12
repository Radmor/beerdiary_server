from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import date

from pubs.models import Pub
from beers.models import Beer

class PubVisit(models.Model):
    pub = models.ForeignKey(Pub, related_name='pubvisits', verbose_name=_('pub'))
    beers = models.ManyToManyField(Beer, related_name='pub_visits', verbose_name=_('beers'))
    date = models.DateField(verbose_name=_('date'), default=date.today)

    def __str__(self):
        return '{}, {}'.format(str(self.date), self.pub)

    class Meta:
        verbose_name = _('Pub visit')
        verbose_name_plural = _('Pub visits')