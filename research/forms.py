from django import forms

from .models import ResearchProject

class ResearchProjectForm(forms.ModelForm):
    class Meta:
        model = ResearchProject
        fields = ('name', 'description', "short_description", 'incharge', 'status', 'domain', 'project_cover_picture')