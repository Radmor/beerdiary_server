from django.db import models
from django.utils.translation import ugettext as _


class Style(models.Model):
    name = models.CharField(_('name'), max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('style')
        verbose_name_plural = _('styles')
