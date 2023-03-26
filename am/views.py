from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Event
from .forms import EventForm

# Home View
class AMHomeView(ListView):
    model = Event
    template_name = 'am/am.html'
    context_object_name = 'events'
    ordering = ['-start_date']

class AMDetailView(DetailView):
    model = Event
    template_name = 'am/am_detail.html'
    context_object_name = 'event'

# Admin views
class EventListView(ListView):
    model = Event
    template_name = 'am/event_list.html'
    context_object_name = 'events'
    ordering = ['-start_date']

class EventDetailView(DetailView):
    model = Event
    template_name = 'am/event_detail.html'
    context_object_name = 'event'

class EventCreateView(CreateView):
    model = Event
    template_name = 'am/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('am:event-list')

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'am/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('am:event-list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'am/event_confirm_delete.html'
    success_url = reverse_lazy('am:event-list')
