from django.forms import ModelForm
from projects.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model  = Project
        fields = ['name', 'hackathon', 'description', 'author', 'min_participants', 'max_participants', 'skills', 'tags']