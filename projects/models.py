from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=240)
    description = models.TextField()
    author = models.CharField(max_length=50)
    participants = models.TextField()
    min_participants = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    max_participants = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    hackathon = models.ForeignKey('Hackathon', on_delete=models.SET_NULL, null=True)
    skills = models.TextField()
    tags = models.TextField()
    def __str__(self):
        return self.name

class Hackathon(models.Model):
    number = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return 'Hackathon {}'.format(self.number)