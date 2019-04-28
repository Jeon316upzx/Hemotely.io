from django.urls import path
from Jobpost import views

urlpatterns =[
   path('jobpost/',views.JobUpload,name='jobupload'),
]
