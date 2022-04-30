from django import forms
from .models import Certrequest

class Request_form(forms.ModelForm):
   class Meta:
       model = Certrequest
       fields = [
           'Resident_code',
           'Email',
           'Purpose',
           'Request_type'
       ]