from django.views import generic

from .models import Game

class GameListView(generic.ListView):
    model = Game
    template_name = "game_list.html"


class GameView(generic.DetailView):
    model = Game
    template_name = "game_detail.html"


class PlayerView(generic.DetailView):
    model = Game
    template_name = "game_player_detail.html"

    def get_context_data(self, **context):
        context_data = super().get_context_data(**context)
        context_data["player"] = self.kwargs["player"]
        context_data["cards"] = list(self.object.get_cards(int(self.kwargs["player"])))
        return context_data
