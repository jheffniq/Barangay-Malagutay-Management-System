from django import forms
from .models import Blotreport


class Blotter_Form(forms.ModelForm):
    class Meta:
        model = Blotreport
        fields = [
            'Complainant',
            'Complaint',
        ]