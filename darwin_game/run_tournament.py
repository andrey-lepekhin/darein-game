from darwin_game.core.import_players import find_import_player_classes
from darwin_game.core.tournament import DarwinGame

players_folder = "darwin_game/players"
player_classes = find_import_player_classes(players_folder, exclude_dirs=[])


tournament = DarwinGame(player_classes=player_classes, rounds=100, initial_player_copies=100, game_turns=100)
tournament.pretty_print_results(tournament.run_tournament())
