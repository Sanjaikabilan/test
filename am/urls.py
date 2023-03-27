from django.urls import path

from . import views

app_name = 'am'

urlpatterns = [
    path('', views.AMHomeView.as_view(), name='am-home'),
    path('<slug:slug>/', views.AMDetailView.as_view(), name='am-detail'),
    # path('admin', views.EventListView.as_view(), name='event-list'),
    # path('admin/create/', views.EventCreateView.as_view(), name='event-create'),
    # path('admin/<slug:slug>/', views.EventDetailView.as_view(), name='event-detail'),
    # path('admin/<slug:slug>/update/', views.EventUpdateView.as_view(), name='event-update'),
    # path('admin/<slug:slug>/delete/', views.EventDeleteView.as_view(), name='event-delete'),
]
