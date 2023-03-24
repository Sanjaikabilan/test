from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.state, name='statements'),
    path('', views.reset, name='reset'),
    path('state/<int:pk>/', views.StateDetail, name='state_detail'),
    path('suc', views.suc, name='suc'),
    path('sum', views.ideasum, name='sum'),
]