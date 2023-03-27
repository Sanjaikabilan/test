from django.urls import path

from . import views

app_name = 'research'

urlpatterns = [
    path('', views.ResearchHomeView.as_view(), name="research-home"),
    path("<int:pk>", views.ResearchDetailView.as_view(), name="research-detail"),
    # path('project/', views.ProjectListView.as_view(), name='project-list'),
    # path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    # path('project/new/', views.ProjectCreateView.as_view(), name='project-create'),
    # path('project/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
    # path('project/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),
]
