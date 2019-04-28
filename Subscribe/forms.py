from . import models
from django import forms

class Subscribe_form(forms.ModelForm):
    Email = forms.EmailField(label = 'Enter Email',required = True, widget = forms.TextInput(attrs ={'class': "form-control"}))
    Name = forms.CharField(label = 'Enter Name',required = True, widget = forms.TextInput(attrs ={'class': "form-control"}))
    class Meta:
        model  = models.Subscribe_model
        fields = ['Email','Name']
