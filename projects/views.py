from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/index.html', context)

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/project.html', {'project':project})
    #HttpResponse("Project %s" % project_id)

def add_project(request):
    return HttpResponse("Adding project")

def edit_project(request, project_id):
    return HttpResponse("Edit project %s" % project_id)