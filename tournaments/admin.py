from django.contrib import admin
from tournaments.models import Player, Team, Tournament
# Register your models here.


admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Tournament)