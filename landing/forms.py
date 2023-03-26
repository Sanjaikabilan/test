from django import forms
from django.core.mail import send_mail
from django.conf import settings
from allauth.account.views import PasswordResetView

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 50)
    message = forms.CharField(max_length = 2000)

    class Meta:
        fields = ('name', 'email', 'message')

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name-1',
                    'placeholder': 'Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email-1',
                    'placeholder': 'Email'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'message-1',
                    'rows': '6',
                    'placeholder': 'Message'
                }
            ),
        }
	
    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        # send email
        send_mail(
            f'Contact Form - {name} - {email}',
            message,
            settings.EMAIL_HOST_USER,
            ['noreply.researchcell@gmail.com'],
            fail_silently=False,
        )
        