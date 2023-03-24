import django_filters

from .models import State

class StateFilter(django_filters.FilterSet):
    class Meta:
        model = State
        fields = ['domain', 'hardness']