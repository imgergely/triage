
from django.forms import ModelForm
from .models import TriageA, TriageB

class TriageAForm(ModelForm):
    class Meta:
        model = TriageA
        fields = '__all__'

class TriageBForm(ModelForm):
    class Meta:
        model = TriageB
        fields = '__all__'