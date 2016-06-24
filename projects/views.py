from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.db.models import Max
from django.contrib.auth.decorators import login_required

from helpers import *
from .models import Project
from .models import Hackathon
from django.contrib.auth.models import User

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

    if request.method == 'POST':
        if "leave" in request.POST:
            project.participating_users.remove(request.user)
            current_user_participating = False
        if "join" in request.POST:
            project.participating_users.add(request.user)
            current_user_participating = True
        redirect_url = "/projects/" + str(project_id)
        return HttpResponseRedirect(redirect_url, {'project':project, 'current_user_participating':current_user_participating})

    if request.user.is_authenticated():
        current_user_participating = request.user.participant.filter(id=project.id).exists()
    else:
        current_user_participating = False

    return render(request, 'projects/project.html', {'project':project, 'current_user_participating':current_user_participating})

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

@login_required
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
