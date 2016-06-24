from datetime import date

from .models import Project
from .models import Hackathon

def get_current_hackathon():
    today = date.today()
    for hackathon in Hackathon.objects.all():
       if hackathon.start_date <= today and hackathon.end_date >= today:
            return hackathon.number