# type: ignore
import cProfile
import pstats

from darwin_game.core.import_players import find_import_player_classes
from darwin_game.core.tournament import DarwinGame


def test_tournament():
    tournament = DarwinGame(
        player_classes=find_import_player_classes("darwin_game/players/simple"),
        rounds=100,
        initial_player_copies=100,
        game_turns=100,
        lowest_pool_percent_for_player=None,
    )
    tournament.pretty_print_results(tournament.run_tournament())


cProfile.run("test_tournament()", "tournament.profile")


p = pstats.Stats("tournament.profile")
p.sort_stats("time").print_stats(10)
