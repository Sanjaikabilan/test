from django import forms

from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'name',
            'description',
            'short_description',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'venue',
            'cover_picture',
            'poster',
            'is_this_a_colab',
            'colab_with',
            'linkedin_post_url',
            'overall_coordinator',
        )

        widgets = {
            'start_date': forms.DateInput(
                attrs={
                'type': 'date'
                }
            ),
            'end_date': forms.DateInput(
                attrs={
                'type': 'date'
                }
            ),
            'start_time': forms.TimeInput(
                attrs={
                'type': 'time'
                }
            ),
            'end_time': forms.TimeInput(
                attrs={
                'type': 'time'
                }
            ),
        }