from django.shortcuts import render

def research(request):
    return render(request, 'research/research.html', {})