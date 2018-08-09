from django import forms
from django.contrib.auth.models import User
from .models import Events,  Notices, Complaints, Staff, Attendance


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaints
        fields = ['name', 'details', 'urgency_level', 'status']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']


