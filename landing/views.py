from django.shortcuts import render
from django.views.generic import FormView

from .forms import ContactForm

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'landing/contact.html'
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
# Create your views here.

def land(request):
    ui = """background: url('{% static 'img/blob-haikei%20(3).svg' %}') top right / auto no-repeat, var(--bs-white);"""
    return render(request, 'landing/land.html', {'ui': ui})
