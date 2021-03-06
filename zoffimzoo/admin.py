from django.contrib import admin

from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ("round", "date", "players")
    readonly_fields = ("cards",)


admin.site.register(Game, GameAdmin)
