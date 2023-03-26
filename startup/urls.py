from django.urls import path

from . import views

app_name = 'startup'

urlpatterns = [
    path('', views.startup, name="startup-home"),
    
    # Startup Project URLs
    path('projects-teams/', views.ProjectTeamListView.as_view(), name='project-team-list'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', views.ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),

    # Startup Team URLs
    path('team/<int:pk>/', views.TeamDetailView.as_view(), name='team-detail'),
    path('team/new/', views.TeamCreateView.as_view(), name='team-create'),
    path('team/<int:pk>/update/', views.TeamUpdateView.as_view(), name='team-update'),
    path('team/<int:pk>/delete/', views.TeamDeleteView.as_view(), name='team-delete'),

]
