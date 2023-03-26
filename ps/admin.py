from django.contrib import admin
from .models import Apply, State, Team, Participants, OwnTeam, OwnParticipants, OwnState


# Register your models here.

admin.site.register(Apply)
admin.site.register(State)
admin.site.register(Team)
admin.site.register(Participants)
admin.site.register(OwnTeam)
admin.site.register(OwnParticipants)
admin.site.register(OwnState)