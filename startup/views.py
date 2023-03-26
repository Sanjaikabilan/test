from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import StartupProject, Team
from .forms import StartupProjectForm, TeamForm

def startup(request):
    return render(request, 'startup/startup.html', {})


class ProjectTeamListView(ListView):
    model = StartupProject
    template_name = 'startup/project/project_team_list.html'
    context_object_name = 'projects'
    ordering = ['-name']
    paginate_by = 5

    # Also add teams to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        return context

# Startup Project Views

class ProjectDetailView(DetailView):
    model = StartupProject
    template_name = 'startup/project/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = StartupProject
    form_class = StartupProjectForm
    template_name = 'startup/project/startup_project_form.html'
    success_url = reverse_lazy('startup:project-team-list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
    
class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = StartupProject
    form_class = StartupProjectForm
    template_name = 'startup/project/startup_project_form.html'
    success_url = reverse_lazy('startup:project-team-list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = StartupProject
    template_name = 'startup/project/project_confirm_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('startup:project-team-list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

# Startup Team Views

class TeamDetailView(DetailView):
    model = Team
    template_name = 'startup/team/team_detail.html'
    context_object_name = 'team'

class TeamCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'startup/team/team_form.html'
    success_url = reverse_lazy('startup:project-team-list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
    
class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'startup/team/team_form.html'
    success_url = reverse_lazy('startup:project-team-list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
    
class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Team
    template_name = 'startup/team/team_confirm_delete.html'
    context_object_name = 'team'
    success_url = reverse_lazy('startup:project-team-list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
    