import random

from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult


class FlexibleStrategist(Player):
    name = "FlexibleStrategist"

    def predict_opponent_next_action(self, turn_history, your_number):
        # Simplified prediction mechanism based on the opponent's recent actions
        if not turn_history:
            return 2  # Default to a cooperative start
        recent_opponent_actions = [turn.actions[1 - your_number] for turn in turn_history[-3:]]
        return max(set(recent_opponent_actions), key=recent_opponent_actions.count)

    def make_turn(self, turn_history: list[TurnResult], your_number: PlayerNumber) -> Action:
        if not turn_history:
            return 2  # Start with a cooperative move

        predicted_opponent_action = self.predict_opponent_next_action(turn_history, your_number)

        # Adjust strategy based on the phase of the game
        game_phase = len(turn_history)
        if game_phase < 20:
            # Early game: Explore opponent's tendencies
            return random.randint(1, 3)
        elif game_phase < 40:
            # Mid game: Start to solidify strategy based on opponent's behavior
            if predicted_opponent_action > 2:
                return max(5 - predicted_opponent_action, 1)
            else:
                return min(predicted_opponent_action + 1, 3)
        else:
            # Late game: Optimize strategy based on established patterns
            if all(turn.actions[1 - your_number] == 2 for turn in turn_history[-5:]):
                # If the opponent has been consistently cooperative, mirror this to maintain balance
                return 3
            elif any(turn.actions[1 - your_number] > 3 for turn in turn_history[-5:]):
                # If the opponent has shown aggression, adopt a defensive posture
                return 2
            else:
                # Otherwise, aim for a balanced approach
                return 2 if game_phase % 2 == 0 else 3
