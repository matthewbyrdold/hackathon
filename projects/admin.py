from django.contrib import admin
from .models import Project
from .models import Hackathon

# Register your models here.
admin.site.register(Hackathon)
admin.site.register(Project)