from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.reg , name='reg'),
    path('<str:hashid>/', views.see , name='see'),
    
]