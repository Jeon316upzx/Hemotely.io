from django import forms
from . import models
from django_countries.data import COUNTRIES

class CreateJob(forms.ModelForm):
    FT = 'Fulltime'
    PT = 'Parttime'
    IN = 'Internship'
    RE = 'Remote'
    workoptions = (('Fulltime',FT),('Parttime',PT),('Internship',IN),('Remote',RE))
    position = forms.CharField(label = 'Position',required = True, widget = forms.TextInput(attrs ={'class': "form-control"}))
    companyName = forms.CharField(label = 'Company Name',required = True, widget = forms.TextInput(attrs ={'class': "form-control"}))
    location = forms.ChoiceField(choices = sorted(COUNTRIES.items()), widget = forms.Select(attrs={'class': "form-control"}))
    category = forms.ChoiceField(choices = workoptions,widget = forms.Select(attrs={'class': "form-control"}))
    companyEmail = forms.EmailField(label = 'Company Email',required = True, widget = forms.TextInput(attrs ={'class': "form-control"}))
    companyApplyUrl = forms.URLField(label = 'Apply Url',required = True, widget = forms.TextInput(attrs ={'class': "form-control"}))
    jobResp = forms.CharField(label = 'Job Responsiblities',required = True, widget = forms.Textarea(attrs ={'class': "form-control"}))
    jobReq = forms.CharField(label = 'Job Requirement',required = True, widget = forms.Textarea(attrs ={'class': "form-control"}))
    jobDesc = forms.CharField(label = 'Job Description',required = True, widget = forms.Textarea(attrs ={'class': "form-control"}))
    salary = forms.IntegerField(label = 'Salary',required = False, widget = forms.TextInput(attrs ={'class': "form-control"}))
    tags = forms.CharField(label = 'Tags',required = True, widget = forms.TextInput(attrs ={'class': "form-control"}))
    class Meta:
        model  = models.Job
        fields = ['position','location','category','companyName','companyLogo','companyEmail','companyApplyUrl','jobResp','jobReq','jobDesc','salary','tags']
