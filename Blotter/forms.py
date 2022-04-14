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

class Blotter_Form_Unregistered(Blotter_Form):
    class Meta(Blotter_Form.Meta):
        fields = [
            'Offender_unregistered',
            'Complainant',
            'Complaint',
            'Facts',
        ]