from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Accounts.models import Official
from django.contrib.auth.models import User
from django import forms

class User_form(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control' }))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control' }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control' }))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control' }))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(User_form, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class Update_user(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control' }))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control' }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control' }))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control' }))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class OfficalForm(forms.ModelForm):
    class Meta:
        model = Official
        fields = [
        'Barangay_Chairman',
        'Barangay_Secretary',
        'Barangay_Treasurer',
        'SK_Chairman'
    ]