from django import forms
from .models import Certrequest

class Request_form(forms.ModelForm):
   class Meta:
       model = Certrequest
       fields = [
           'Email',
           'Purpose'
       ]