from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Hackathon
from .forms import HackathonForm

def index(request):
    hackathons = Hackathon.objects.all()
    context = {'hackathons': hackathons}
    return render(request, 'hackathons/index.html', context)
    #return HttpResponse("Hello, world. You're at the hackathon index")
    
def add_hackathon(request):
    form = HackathonForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            hackathon = form.save(commit=False)
            hackathon.save()
            return HttpResponseRedirect("/projects/")
    context = {
        "form": form
    }
    
    return render(request, "hackathons/add.html", context)

def edit_hackathon(request, number):
    hackathon = get_object_or_404(Hackathon, pk=number)
    form = HackathonForm(request.POST or None, instance=hackathon)
    if form.is_valid():
        hackathon = form.save(commit=False)
        hackathon.save()
        return HttpResponseRedirect("/projects/")

    context = {
        "form": form,
        "hackathon": hackathon
    }

    return render(request, "hackathons/edit.html", context)