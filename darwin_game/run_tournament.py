import logging

from darwin_game.core.import_players import find_import_player_classes
from darwin_game.core.tournament import DarwinGame, MatchupType

logging.basicConfig(level=logging.INFO)  # set to DEBUG for more info. Will break pretty print

players_folder = "darwin_game/players"
player_classes = find_import_player_classes(players_folder, exclude_dirs=["chat_gpt", "simple"])

player_classes = find_import_player_classes(players_folder, include_dirs)


tournament = DarwinGame(
    player_classes=player_classes,
    rounds=50,
    initial_player_copies=20,
    game_turns=100,
    matchup_type=MatchupType.RANDOM_PAIRING,
)
tournament.pretty_print_results(tournament.run_tournament())
