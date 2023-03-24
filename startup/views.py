from django.shortcuts import render

def startups(request):
    return render(request, 'startup/startup.html', {})