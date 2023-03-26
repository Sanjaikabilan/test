from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import ResearchProject
from .forms import ResearchProjectForm

def research(request):
    return render(request, 'research/research.html', {})

class ResearchHomeView(ListView):
    model = ResearchProject
    template_name = 'research/research.html'
    context_object_name = 'projects'
    paginate_by = 5

class ResearchDetailView(DetailView):
    model = ResearchProject
    template_name = 'research/research_detail.html'
    context_object_name = 'project'

class ProjectListView(ListView):
    model = ResearchProject
    template_name = 'research/project_list.html'
    context_object_name = 'projects'
    paginate_by = 5

class ProjectDetailView(DetailView):
    model = ResearchProject
    template_name = 'research/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ResearchProject
    form_class = ResearchProjectForm
    template_name = 'research/research_project_form.html'
    success_url = reverse_lazy('research:project-list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
    
class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ResearchProject
    form_class = ResearchProjectForm
    template_name = 'research/research_project_form.html'
    success_url = reverse_lazy('research:project-list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ResearchProject
    template_name = 'research/project_confirm_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('research:project-list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False