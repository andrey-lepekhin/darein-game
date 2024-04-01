import random
from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult


class StrategosBot(Player):
    """A strategic player that adapts to opponent's behavior."""

    name: str = "StrategosBot"

    @staticmethod
    def make_turn(turn_history: list[TurnResult], your_number: PlayerNumber) -> Action:
        # First move logic - start with a randomized move of 2 or 3
        if not turn_history:
            return random.choice([2, 3])

        # Analyze opponent's past actions to determine their strategy
        opponent_actions = [turn.actions[1 - your_number] for turn in turn_history]
        opponent_last_action = opponent_actions[-1]

        # Attempt to detect self or highly cooperative patterns
        if len(turn_history) >= 4 and all(a == b for a, b in zip(opponent_actions[-4:], [2, 3, 2, 3])):
            return 3 if (len(turn_history) + 1) % 2 == 0 else 2  # Alternate for maximum cooperation

        # Basic strategy adaptation based on opponent's last action
        if opponent_last_action in [0, 1, 2]:  # Assume cooperative or weaker strategy
            return 3  # Aim for a higher share assuming opponent might play low
        elif opponent_last_action in [3, 4, 5]:  # Assume aggressive or stronger strategy
            return 2  # Play safer to avoid overcommitting and getting nothing

        # Default action if none of the above conditions are met
        return 2  # Lean towards safety in ambiguous situations