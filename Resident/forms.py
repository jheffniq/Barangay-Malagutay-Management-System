from django import forms
from .models import Resident, CSV, TempResident, Household
from django_select2 import forms as s2forms

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
            'Email',
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

class MembersWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "First_name__icontains",
        "Middle_name__icontains",
        "Last_name__icontains"
    ]
class HeadWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "First_name__icontains",
        "Middle_name__icontains",
        "Last_name__icontains"
    ]

class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        widgets = {'Member' : MembersWidget,'Head' : HeadWidget, 'Date' : DateInput()}
        fields = [
            'Head',
            'Date',
            'Contact',
            'Address',
            'Homeowner',
            'Income',
            'Member'
        ]