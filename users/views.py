from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.contrib.auth.models import User
from .forms import EditProfilePageForm, EditSettingsForm

class EditProfilePageView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile.html"
    form_class = EditProfilePageForm

    def get_object(self):
        UserName= self.kwargs.get("slug")
        userObject = get_object_or_404(User, username=UserName)
        page_user = get_object_or_404(Profile, id=userObject.profile.id)
        return page_user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = "registration/show_profile.html"

    def dispatch(self, request, *args, **kwargs):
        UserEmail = request.user.email
        allauthEmail = self.request.user.emailaddress_set.all()[0]
        if str(allauthEmail) != UserEmail:
            allauthEmail.change(request, UserEmail)
            return redirect('account_email_verification_sent')
            
        if request.user.profile.firstname:
            return super().dispatch(request, *args, **kwargs)
        return redirect('edit_profile_page', request.user.username)

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        UserName= self.kwargs.get("slug")
        userObject = get_object_or_404(User, username=UserName)
        page_user = get_object_or_404(Profile, id=userObject.profile.id)
        context['page_user'] = page_user
        return context

class error_404(generic.TemplateView):
    template_name = "users/error_404.html"

class EditSettingsView(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = "registration/edit_settings.html"
    form_class = EditSettingsForm
    userName = None
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):

        UserName= self.kwargs.get("slug")
        self.userName = UserName
        page_user = get_object_or_404(User, username=UserName)
        if page_user.username == request.user.username:
            return super().dispatch(request, *args, **kwargs)
        raise Http404()

    def get_object(self):
        UserName= self.kwargs.get("slug")
        userObject = get_object_or_404(User, username=UserName)
        return userObject

    def get_context_data(self, *args, **kwargs):
        context = super(EditSettingsView, self).get_context_data(*args, **kwargs)
        UserName= self.kwargs.get("slug")
        self.userName = UserName
        page_user = get_object_or_404(User, username=UserName)
        context['page_user'] = page_user
        return context

    def form_valid(self, form):
        self.userName = form.cleaned_data['username']
        self.success_url = reverse_lazy("show_profile_page", kwargs={'slug': self.userName})
        return super().form_valid(form)