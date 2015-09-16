from django.contrib import admin

from .models import Tournament, Player, Game, Result

admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Result)