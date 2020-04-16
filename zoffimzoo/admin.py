from django.contrib import admin

from .models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ("date", "players")
    #fields = ("date", "players", "cards")
    readonly_fields = ("cards",)


admin.site.register(Game, GameAdmin)
