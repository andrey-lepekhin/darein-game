from collections import Counter

import numpy as np

from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult


class Predictive(Player):
    name = "Predictive"

    def predict_opponent_next_action(self, turn_history, your_number):
        """Predicts opponent's next action based on historical frequencies."""
        if not turn_history:
            return 2  # Default starting action if no history

        opponent_actions = [turn.actions[1 - your_number] for turn in turn_history]
        action_frequencies = Counter(opponent_actions)
        return action_frequencies.most_common(1)[0][0]

        # Predict that the opponent will play the most common action again

    def make_turn(self, turn_history: list[TurnResult], your_number: PlayerNumber) -> Action:
        predicted_opponent_action = self.predict_opponent_next_action(turn_history, your_number)

        # Strategy for self-play
        if all(turn.actions[0] == turn.actions[1] for turn in turn_history if turn_history):
            # In case of self-play, alternate between 2 and 3 to maximize score
            return 2 if len(turn_history) % 2 == 0 else 3

        # Dynamic strategy based on predicted opponent action
        if predicted_opponent_action in [0, 1]:
            # Opponent plays low, we play high for maximum gain
            return 5 - predicted_opponent_action
        elif predicted_opponent_action in [4, 5]:
            # Opponent plays high, we play conservatively
            return 1
        else:
            # In case of a moderate opponent, alternate between playing 2 and 3 to aim for cooperation
            # or adjust based on the game phase to be more aggressive or defensive
            current_phase = len(turn_history) // 10
            if current_phase < 5:
                # Early to mid-game: slightly more aggressive to build up points
                return 3 if np.random.rand() > 0.5 else 2
            else:
                # Late game: more conservative to avoid losses
                return 2
