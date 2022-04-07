from django import forms
from .models import Resident, CSV

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
            'Birthdate',
            'Gender',
            'Marital_status',
            'Contact',
            'Citizenship',
            'Religion',
            'Occupation',
            'Vaccination',
            'Address',   
        ]

class CSVmodel(forms.ModelForm):
    class Meta:
        model = CSV
        fields = [
            'file_name'
        ]