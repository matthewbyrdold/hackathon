from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("List of projects")

def project(request, project_id):
    return HttpResponse("Project %s" % project_id)

def add_project(request):
    return HttpResponse("Adding project")

def edit_project(request, project_id):
    return HttpResponse("Edit project %s" % project_id)