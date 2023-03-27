from django import forms
from django.contrib.auth.models import User
from .models import Profile

class EditProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'firstname',
            'lastname',
            'gender',
            'date_of_birth'
        )

        widgets = {
            'firstname': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                    'id': 'dob'
                }
            ),
            'gender': forms.Select(),
        }

class EditSettingsForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Your username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    'placeholder': 'Your e-mail address'
                }
            ),
        }
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == self.instance.username:
            return username
        if username.isdigit():
            raise forms.ValidationError("Username cannot be all numbers.")
        if not username.isalnum():
            raise forms.ValidationError("Username can have only alphabets and numbers.")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username {}'s already taken.".format(username))
        return username