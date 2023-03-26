from django.contrib import admin
from .models import Apply, State, Team, Participants


# Register your models here.

admin.site.register(Apply)
admin.site.register(State)
admin.site.register(Team)
admin.site.register(Participants)