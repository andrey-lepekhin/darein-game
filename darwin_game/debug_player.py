import logging

from darwin_game.core.tournament import DarwinGame, MatchupType
from darwin_game.core.game import Game
from darwin_game.models.player import Player
from darwin_game.players.andrey.practic2 import Practic2 as DebuggedPlayer


# logging.basicConfig(level=logging.DEBUG)


# Test self-play
SELF_PLAY_ROUNDS = 1


class DebuggedPlayerCopy(DebuggedPlayer):
    name = DebuggedPlayer.name + " Copy"


self_play_results: list[dict[Player, int]] = []
player1 = DebuggedPlayer()
player2 = DebuggedPlayerCopy()
self_play_game = Game(player1=player1, player2=player2, max_turns=100)
for _ in range(SELF_PLAY_ROUNDS):
    self_play_results.append(self_play_game.play_game())
average_self_play_score = sum(result[player1] + result[player2] for result in self_play_results) / len(
    self_play_results
)
max_possible_score = self_play_game.max_turns * 5
print(f"Average self-play score: {average_self_play_score}. Max possible score: {max_possible_score}")


# Test against an opponent
