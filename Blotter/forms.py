from django import forms
from .models import Blotreport


class Blotter_Form(forms.ModelForm):
    class Meta:
        model = Blotreport
        fields = [
            'Complainant',
            'Complaint',
            'Facts',
        ]
    def __init__(self, *args, **kwargs):
        super(Blotter_Form, self).__init__(*args, **kwargs)
        self.fields['Complainant'].label = "Complainant"
        self.fields['Facts'].help_text = "Please separate each bullet point with a comma."

class Blotter_Form_Unregistered(Blotter_Form):
    class Meta(Blotter_Form.Meta):
        fields = [
            'Offender_unregistered',
            'Complainant',
            'Complaint',
            'Facts',
        ]