
from django.forms import ModelForm
from .models import Triage

class TriageForm(ModelForm):
    class Meta:
        model = Triage
        exclude = ('user',)

