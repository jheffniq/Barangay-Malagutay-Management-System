from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Accounts.models import Official
from django.contrib.auth.models import User
from django import forms

class User_form(UserCreationForm):

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


class Update_user(forms.ModelForm):

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
        'Barangay_Councilors',
        'SK_Chairman',
        'SK_Councilors'
    ]
    def __init__(self, *args, **kwargs):
        super(OfficalForm, self).__init__(*args, **kwargs)
        self.fields['Barangay_Councilors'].help_text = "Please separate each name with a comma."
        self.fields['SK_Councilors'].help_text = "Please separate each name with a comma."