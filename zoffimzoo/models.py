import random

from django.core import validators
from django.db import models
from django.utils.formats import localize
from django.utils.timezone import localtime

from .cards import ALL_CARDS


class Game(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    round = models.CharField(max_length=255)

    players = models.CharField(max_length=255)

    cards = models.TextField(editable=False, null=True)

    def __str__(self):
        return f"{self.round}: {localize(localtime(self.date))}"

    def save(self, *args, **kwargs):
        if self.pk is None:
            cards = ALL_CARDS.copy()
            random.shuffle(cards)
            self.cards = ",".join([card.name for card in cards])
        super().save(*args, **kwargs)

    @property
    def players_list(self):
        return [(i + 1, player) for i, player in enumerate(self.players.split(","))]

    def get_cards(self, player):
        all_cards = self.cards.split(",")
        for i, card in enumerate(all_cards):
            if i % len(self.players.split(",")) == player - 1:
                yield card

    def get_player_name(self, position):
        return self.players.split(",")[position]
