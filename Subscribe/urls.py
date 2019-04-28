from django.contrib import admin
from django.urls import path
from Subscribe import views

urlpatterns = [
    path('subscribe/', views.Sub,name ='suburl'),

]
