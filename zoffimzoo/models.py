import random

from django.core import validators
from django.db import models

from .cards import ALL_CARDS


class Game(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    players = models.PositiveIntegerField(
        default=4,
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(7)],
    )

    cards = models.TextField(editable=False, null=True)

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        if self.pk is None:
            cards = ALL_CARDS.copy()
            random.shuffle(cards)
            self.cards = ",".join([card.name for card in cards])
        super().save(*args, **kwargs)

    @property
    def players_list(self):
        return [i+1 for i in range(self.players)]

    def get_cards(self, player):
        all_cards = sorted(self.cards.split(","))
        for i, card in enumerate(all_cards):
            if i % self.players == player-1:
                print("Hier", card)
                yield card
