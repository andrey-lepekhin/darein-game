import numpy as np

from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult


class QuantumStrategist(Player):
    name = "QuantumStrategist"

    def __init__(self):
        self.strategy_mode = "initial"
        self.prediction_accuracy = 0.75  # Simulate high predictive accuracy

    def predict_opponent_action(self, turn_history, your_number):
        """A heuristic-based predictive model simulating advanced analysis."""
        if not turn_history:
            return 2  # Default cooperative start
        opponent_actions = [turn.actions[1 - your_number] for turn in turn_history]
        most_common_action = max(set(opponent_actions), key=opponent_actions.count)
        # Introduce a randomness factor to simulate prediction uncertainty
        if np.random.rand() > self.prediction_accuracy:
            return np.random.randint(0, 6)  # Simulate incorrect prediction occasionally
        return most_common_action

    def select_strategy(self, turn_history, your_number):
        """Selects the strategy based on game phase and opponent behavior."""
        game_phase = len(turn_history)
        if game_phase < 20:
            self.strategy_mode = "aggressive"
        elif game_phase < 40:
            self.strategy_mode = "adaptive"
        else:
            self.strategy_mode = "conservative"

    def make_turn(self, turn_history: list[TurnResult], your_number: PlayerNumber) -> Action:
        predicted_action = self.predict_opponent_action(turn_history, your_number)
        self.select_strategy(turn_history, your_number)

        if self.strategy_mode == "aggressive":
            return min(predicted_action + 1, 5)  # Push the boundary early on
        elif self.strategy_mode == "adaptive":
            # Adapt strategy based on predicted opponent action
            if predicted_action <= 2:
                return 3  # Capitalize on conservative play
            else:
                return 2  # Play safe against aggression
        else:  # 'conservative'
            # In the late game, focus on securing points without risks
            if predicted_action >= 3:
                return 2  # Avoid overreaching
            else:
                return predicted_action  # Mirror opponent in conservative play
