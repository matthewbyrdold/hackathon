from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.db.models import Max
from datetime import date

from .models import Project
from .models import Hackathon
from .forms import ProjectForm

def getCurrentHackathon():
    today = date.today()
    for hackathon in Hackathon.objects.all():
        if hackathon.start_date <= today and hackathon.end_date >= today:
            return hackathon.number

def index(request, hackathon = getCurrentHackathon()):
    projects = Project.objects.all() # TODO: only get projects in current hackathon
    context = {'projects': projects, 'hackathon':hackathon}
    return render(request, 'projects/index.html', context)

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/project.html', {'project':project})

def add_project(request):
    form = ProjectForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return HttpResponseRedirect("/projects/")
    context = {
        "form": form
    }
    
    return render(request, "projects/add.html", context)

def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        project = form.save(commit=False)
        project.save()
        return HttpResponseRedirect("/projects/")

    context = {
        "form": form,
        "project": project
    }

    return render(request, "projects/edit.html", context)
