from django.forms import ModelForm
from hackathons.models import Hackathon

class HackathonForm(ModelForm):
    class Meta:
        model  = Hackathon
        fields = ['number', 'start_date', 'end_date']