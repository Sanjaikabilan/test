from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.land, name='land' )
    path('contact', views.ContactView.as_view(), name='contact'),
]
