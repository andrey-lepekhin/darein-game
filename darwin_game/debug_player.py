import logging

from tqdm.auto import trange

from darwin_game.core.game import Game

from darwin_game.players.andrey.practic2 import Practic2 as DebuggedPlayer


logging.basicConfig(level=logging.DEBUG)


# Test self-play
SELF_PLAY_ROUNDS = 1


class DebuggedPlayerCopy(DebuggedPlayer):
    name = DebuggedPlayer.name + " Copy"


self_play_results = []
player1 = DebuggedPlayer()
player2 = DebuggedPlayerCopy()
self_play_game = Game(player1=player1, player2=player2, max_turns=100)
for _ in trange(SELF_PLAY_ROUNDS):
    self_play_results.append(self_play_game.play_game())
average_self_play_score = sum(result[player1] + result[player2] for result in self_play_results) / len(
    self_play_results
)
max_possible_score = self_play_game.max_turns * 5
print(f"Average self-play score: {average_self_play_score}. Max possible score: {max_possible_score}")


# Test against an opponent
ROUNDS_WITH_OPPONENT = 1000
from darwin_game.players.tony.clippy import Clippy as Opponent

player1 = DebuggedPlayer()
player2 = Opponent()
game_results = []

game_with_opponent = Game(player1=player1, player2=player2, max_turns=100, debug_per_turn_results=True)
for _ in trange(ROUNDS_WITH_OPPONENT):
    game_with_opponent.play_game()
    game_results.append(game_with_opponent.play_game())
debugged_player_avg_score = sum(result[player1] for result in game_results) / len(game_results)
opponent_avg_score = sum(result[player2] for result in game_results) / len(game_results)
print(f"{player1.name} VS {player2.name} avg scores: {debugged_player_avg_score}:{opponent_avg_score}")
