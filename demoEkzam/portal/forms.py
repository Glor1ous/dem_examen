# portal/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import ViolationReport

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

class ViolationReportForm(forms.ModelForm):
    class Meta:
        model = ViolationReport
        fields = ['car_number', 'description']
