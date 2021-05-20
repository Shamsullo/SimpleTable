from django.db import models
from django.utils.translation import ugettext_lazy as _


class SimpleTable(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=120,)
    quantity = models.IntegerField(verbose_name=_('Quantity'))
    distance = models.FloatField(verbose_name=_('Distance'))
    time_stamp = models.DateTimeField(verbose_name=_('Date'))

    def __str__(self):
        return self.name

