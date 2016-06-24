from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.db.models import Max
from django.contrib.auth.decorators import login_required

from helpers import *
from .models import Project
from .models import Hackathon
from .forms import ProjectForm

def index(request, hackathon = decide_which_hackathon_to_display()):
    if hackathon:
        projects = Project.objects.filter(hackathon__number = hackathon)
    else:
        projects = Project.objects.all()
    hackathons = decide_which_hackathons_to_display(4)
    context = {'projects': projects, 'hackathon': hackathon, 'hackathons': hackathons}
    return render(request, 'projects/index.html', context)

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/project.html', {'project':project})

@login_required
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
