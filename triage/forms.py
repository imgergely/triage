
from django.forms import ModelForm
from .models import Triage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

class TriageForm(ModelForm):
    class Meta:
        model = Triage
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white'),
                Reset('reset', 'Reset Form', css_class='button white'),),)