from crispy_forms.bootstrap import Tab, TabHolder
from django.forms import ModelForm
from .models import Triage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from django import forms


LEGUT_CHOICES = (
        ('1', 'Átjárható',),
        ('2', 'Elzáródott',),
        ('3', 'Stidoros',),
        ('4', 'Zörgő, szörcsögő',),
        ('5', 'Sípoló',),
        ('6', 'Horkoló',),
    )

class TriageForm(ModelForm):
    class Meta:
        model = Triage
        exclude = ('user',)

    def clean_region(self):
        if len(self.cleaned_data['legut']) > 1:
            raise forms.ValidationError('Select only 1 option.')
        return self.cleaned_data['legut']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['legut']= forms.MultipleChoiceField(choices=LEGUT_CHOICES, widget=forms.CheckboxSelectMultiple())
        self.fields['kohoges'].widget.attrs.update({'style': 'display: none'})

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('', 'patientid'),
            Fieldset('A', 'legut'),
            Fieldset('B',   Row(
                                Column('legzesszam', css_class='form-group col-md-6 mb-0'),
                                Column('legzesszam_LF', css_class='form-group col-md-6 mb-0'),
                                css_class='form-row'
                                ),
                            Row(
                                Column('legzesi_munka', css_class='form-group col-md-6 mb-0'),
                                Column('legzesi_munka_SPO', css_class='form-group col-md-6 mb-0'),
                                css_class='form-row'
                                ),
                            Row(Column('kohoges', css_class='form-group col-md-6 mb-0'),
                                css_class='form-row'
                                ),),
            Fieldset('C',   Row(
                                Column('pulzus', css_class='form-group col-md-6 mb-0'),
                                Column('pulzus_p', css_class='form-group col-md-6 mb-0'),
                                css_class='form-row'
                                ),
                            Row(
                                Column('bor', css_class='form-group col-md-6 mb-0'),
                                Column('crt', css_class='form-group col-md-6 mb-0'),
                                Column('rrbo', css_class='form-group col-md-6 mb-0'),
                                css_class='form-row'
                                ),),
            Fieldset('',   
                            Row(
                                Column('triage_category', css_class='form-group col-md-6 mb-0'),
                                css_class='form-row'
                                ),),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white'),
                Reset('reset', 'Reset Form', css_class='button white'),),)

                