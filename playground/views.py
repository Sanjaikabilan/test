from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import TesTeam
import random


# Create your views here.

def reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        team = TesTeam(name=name, email=email, phone=phone)
        team.save()
        return HttpResponseRedirect(reverse('see', args=[team.hashid]))
    return render(request, 'playground/reg.html')

def see(request, hashid):

    team = get_object_or_404(TesTeam, hashid=hashid)
    return render(request, 'playground/see.html', {'team': team})


