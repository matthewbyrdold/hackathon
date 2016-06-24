from __future__ import unicode_literals

import re

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Hackathon(models.Model):
    number = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return 'Hackathon {}'.format(self.number)
