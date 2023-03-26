from django.urls import path
from .views import EditProfilePageView, EditSettingsView, ShowProfilePageView

urlpatterns = [
    # path('', home, name="home"),
    path('@<slug:slug>', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('@<slug:slug>/edit_profile', EditProfilePageView.as_view(), name="edit_profile_page"),
    path('@<slug:slug>/settings', EditSettingsView.as_view(), name="edit_settings_page"),
]