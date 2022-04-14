from django import forms
from .models import Resident, CSV, TempResident

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
            'Philhealth_membership',
            'Citizenship',
            'Religion',
            'Occupation',
            'Vaccination',
            'Address',   
        ]

class CSVmodel(forms.ModelForm):

    file_name = forms.FileField(widget=forms.FileInput(attrs={'accept' : ".csv"}))
    class Meta:
        model = CSV
        fields = [
            'file_name'
        ]    


class Temp_Form(forms.ModelForm):

    class Meta:
        widgets = {
            'Birthdate' : DateInput()
        }
        model = TempResident
        fields = [
            'pic',
            'First_name',
            'Middle_name',
            'Last_name',
            'Email',
            'Birthdate',
            'Gender',
            'Marital_status',
            'Contact',
            'Philhealth_membership',
            'Citizenship',
            'Religion',
            'Occupation',
            'Vaccination',
            'Address',   
        ]
