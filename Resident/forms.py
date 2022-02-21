from django import forms
from .models import Resident

class DateInput(forms.DateInput):
    input_type = 'date'


class Resident_Form(forms.ModelForm):
    class Meta:
        widgets = {
            'Birthdate' : DateInput()
        }
        model = Resident
        fields = [
            'pic',
            'First_name',
            'Middle_name',
            'Last_name',
            'Age',
            'Birthdate',
            'Gender',
            'Contact',
            'Citizenship',
            'Religion',
            'Occupation',
            'Vaccination',
            'Address',   
        ]