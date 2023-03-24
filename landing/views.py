from django.shortcuts import render

# Create your views here.

def land(request):
    ui = """background: url('{% static 'img/blob-haikei%20(3).svg' %}') top right / auto no-repeat, var(--bs-white);"""
    return render(request, 'landing/land.html', {'ui': ui})
