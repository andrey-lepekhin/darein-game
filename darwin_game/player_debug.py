import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from darwin_game.players.andrey.practic2 import Practic2 as DebuggedPlayer
# from darwin_game.players.old_guard.rocket import Rocket as DebuggedPlayer

from darwin_game.core.game import Game


class DebuggedPlayer2(DebuggedPlayer):
    name = "DebuggedPlayer2"


rounds = 10000
turns = 100

# Test self-play efficiency
results = []
game = Game(DebuggedPlayer, DebuggedPlayer2, turns)
for _ in range(rounds):

    results.append(game.play_game())

# print average points won in self-play
print(sum([result[DebuggedPlayer] + result[DebuggedPlayer2] for result in results]) / rounds)

print(f"Ideal result is {turns*5}")


# test against another player
from darwin_game.players.tony.clippy import Clippy as AnotherPlayer

game = Game(DebuggedPlayer, AnotherPlayer, turns)

# results = []
# for _ in range(1000):
#     results.append(game.play_game())
#     print(results[-1])

# game.play_game()
# print(game._get_results())

# exit(1)

from darwin_game.core.tournament import DarwinGame

tournament = DarwinGame(
    player_classes=[DebuggedPlayer, AnotherPlayer], rounds=100, initial_player_copies=20, game_turns=100
)
# tournament.debug_player(DebuggedPlayer)
# tournament.pretty_print_results(tournament.run_tournament())
