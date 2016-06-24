from __future__ import unicode_literals

import re

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from hackathons.models import Hackathon

@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=240)
    description = models.TextField()
    author = models.CharField(max_length=50)
    participants = models.TextField(blank=True)
    participating_users = models.ManyToManyField(User, related_name='participant')
    min_participants = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    max_participants = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    hackathon = models.ForeignKey(Hackathon, on_delete=models.SET_NULL, null=True, blank=True)
    skills = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    def __str__(self):
        return self.name

    def participants_as_list(self):
        return filter(bool, re.split('[,;]', self.participants))

    def participants_count(self):
        return len(self.participants_as_list())

    def spaces_left(self):
        return self.participants_count() < self.max_participants

    def participants_needed(self):
        return self.participants_count() > self.min_participants

    def tag_list(self):
        return filter(bool, re.split('[,;]', self.tags))

    def skills_list(self):
        return filter(bool, re.split('[,;]', self.skills))


