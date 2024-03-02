import numpy as np

from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult


class MasterStrategist(Player):
    name = "MasterStrategist"

    def __init__(self):
        self.random_factor = 0.1  # Initial randomness in the strategy

    def analyze_opponent_behavior(self, turn_history, your_number):
        """Analyzes opponent's behavior to adjust the strategy dynamically."""
        if len(turn_history) < 5:
            return np.random.randint(2, 4)  # Start with a mix of cooperation and mild aggression

        opponent_actions = np.array([turn.actions[1 - your_number] for turn in turn_history])
        my_actions = np.array([turn.actions[your_number] for turn in turn_history])

        # Calculate the tendency of the opponent to play aggressively
        opponent_aggressiveness = np.mean(opponent_actions > 2)

        # Adjust the strategy based on the phase of the game and opponent's behavior
        game_phase = len(turn_history)
        if game_phase <= 20:
            # In early game, be slightly more aggressive to build up points
            return 3 if np.random.rand() > self.random_factor else 2
        elif game_phase <= 40:
            # In mid-game, adjust strategy based on opponent's aggressiveness
            if opponent_aggressiveness > 0.5:
                # If opponent is aggressive, increase randomness to confuse them
                self.random_factor = min(self.random_factor + 0.1, 0.5)
                return 2 if np.random.rand() > opponent_aggressiveness else 3
            else:
                # If opponent is not aggressive, play more cooperatively
                return 2 if np.random.rand() > 0.5 else 3
        else:
            # In late game, focus on precision and minimizing risks
            self.random_factor = 0  # Reduce randomness
            if np.mean(my_actions) > np.mean(opponent_actions):
                # If leading, play conservatively
                return 2
            else:
                # If trailing or close, take calculated risks
                return 3 if np.random.rand() > 0.5 else 2

    def make_turn(self, turn_history: list[TurnResult], your_number: PlayerNumber) -> Action:
        return self.analyze_opponent_behavior(turn_history, your_number)
