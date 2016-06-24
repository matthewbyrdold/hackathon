from datetime import date
from django.db.models import Count

from .models import Project
from .models import Hackathon

def get_current_hackathon(today):
    for hackathon in Hackathon.objects.all():
       if hackathon.start_date <= today and hackathon.end_date >= today:
            return hackathon.number
            
def get_upcoming_hackathon(today):
    hackathons = Hackathon.objects.all()
    found_upcoming = False
    if hackathons.count > 0:
        upcoming = hackathons[0]
        
        for hackathon in hackathons:
            if hackathon.start_date >= today and hackathon.start_date <= upcoming.start_date:
                found_upcoming = True
                upcoming = hackathon
        
        if found_upcoming:
            return upcoming.number

def get_previous_hackathon(today):
    hackathons = Hackathon.objects.all()
    found_latest = False
    if hackathons.count > 0:
        latest = hackathons[0]
        
        for hackathon in hackathons:
            if (hackathon.end_date <= today) and (hackathon.end_date >= latest.end_date):
                found_latest = True
                latest = hackathon
                
        if found_latest:
            return latest.number

def decide_which_hackathons_to_display(number):
    return Hackathon.objects.values('number').annotate(start_date_count=Count('start_date')).order_by('-start_date_count')[:number]

def decide_which_hackathon_to_display():
    today = date.today()
    hackathon = get_current_hackathon(today)
    if hackathon != None:
        return hackathon
    else:
        hackathon = get_upcoming_hackathon(today)
        if hackathon != None:
            return hackathon
        else:
            hackathon = get_previous_hackathon(today)
            if hackathon != None:
                return hackathon
