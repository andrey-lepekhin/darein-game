from time import perf_counter
from dataclasses import dataclass, field
import logging

from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class Game:
    player1: Player
    player2: Player
    max_turns: int
    per_turn_results: bool = False

    turn_history: list[TurnResult] = field(default_factory=list[TurnResult], init=False)
    turn_number: int = field(default=0, init=False)

    def _get_turn_result(self, player1_action: Action, player2_action: Action) -> TurnResult:
        # if sum of actions is > 5, both players get 0 as result
        # if sum of actions is <= 5, the players get their respective actions as result
        sum_actions = player1_action + player2_action
        if sum_actions > 5:
            player1_result = 0
            player2_result = 0
        else:
            player1_result = player1_action
            player2_result = player2_action
        return TurnResult(
            (player1_action, player2_action),
            (player1_result, player2_result),  # type: ignore[arg-type]
        )

    def _make_safe_play_turn(self, player: Player, timeout_seconds: float = 0.0003) -> Action:
        player_number = PlayerNumber.PLAYER1 if self.player1 == player else PlayerNumber.PLAYER2

        start_time = perf_counter()
        try:
            turn_action = player.make_turn(self.turn_history, player_number)

            elapsed_time = perf_counter() - start_time
            if elapsed_time > timeout_seconds:
                raise TimeoutError(f"{player} took more than {timeout_seconds} seconds to make a turn.")

            if not 0 <= turn_action <= 5:
                raise ValueError(f"{player} returned a non-Action object: {turn_action}")
            return turn_action
        except Exception as e:
            logger.debug(f"{player} failed with error: {e}. Counting that as a 0 action.")
            return 0

    def _play_turn(self) -> None:
        player1_action = self._make_safe_play_turn(self.player1)
        player2_action = self._make_safe_play_turn(self.player2)
        if self.per_turn_results:
            logger.debug(
                f"{self.turn_number}: {self.player1.name}: {player1_action}, {self.player2.name}: {player2_action}"
            )

        results = self._get_turn_result(player1_action, player2_action)

        self.turn_history.append(results)

        self.turn_number += 1

    def _get_results(self) -> dict[Player, int]:
        player1_score = 0
        player2_score = 0
        for turn in self.turn_history:
            player1_score += turn.results[PlayerNumber.PLAYER1]
            player2_score += turn.results[PlayerNumber.PLAYER2]
        return {self.player1: player1_score, self.player2: player2_score}

    def _reset_game(self) -> None:
        self.turn_history = []
        self.turn_number = 0

    def play_game(self) -> dict[Player, int]:
        self._reset_game()
        while self.turn_number < self.max_turns:
            self._play_turn()
        return self._get_results()
