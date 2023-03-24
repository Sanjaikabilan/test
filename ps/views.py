from django.shortcuts import render
from . models import Apply, State
from . filters import StateFilter

# Create your views here.

def state(request):
    a = State.objects.all()

    myFilter = StateFilter(request.GET, queryset=a)
    a = myFilter.qs
    return render(request,'ps/state.html', {'a':a,'myFilter':myFilter})

def reset(request):

    if request.method == 'GET':
        a = State.objects.all()
    return render(request,'ps/state.html', {'a':a})

def StateDetail(request, pk):
    a = State.objects.get(id=pk)
    contact = a.contact
    ps = a.problem
    des = a.description
    dom = a.domain
    hard = a.hardness
    cp = a.contact_person
    return render(request,'ps/state_detail.html', {'a':a, 'contact':contact, 'ps':ps, 'des':des, 'dom':dom, 'hard':hard, 'cp':cp})

def suc(request):
    return render(request, 'ps/suc.html')

def ideasum(request):
    return render(request, 'ps/sum.html')



