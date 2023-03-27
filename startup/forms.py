from django import forms

from .models import StartupProject, Team

class StartupProjectForm(forms.ModelForm):
    class Meta:
        model = StartupProject
        fields = ('name', 'description', 'team', 'incharge', 'status', 'domain', 'project_cover_picture')

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'description', 'origin_story')