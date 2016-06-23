from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect

from .models import Project
from .forms import ProjectForm

def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
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
