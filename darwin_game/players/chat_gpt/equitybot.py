from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult


class EquityBot(Player):
    name = "EquityBot"

    def make_turn(self, turn_history: list[TurnResult], your_number: PlayerNumber) -> Action:
        # Detect aggressive opponent behavior based on past turns
        if len(turn_history) > 3:  # Give some time to establish pattern
            aggressive_moves = sum(1 for turn in turn_history[-3:] if turn.actions[1 - your_number] >= 4)
            self.aggressive_opponent_detected = (
                aggressive_moves >= 2
            )  # Considered aggressive if at least 2 out of 3 last moves are 4 or more

        if not turn_history:
            return 3 if your_number == PlayerNumber.PLAYER1 else 2

        if self.aggressive_opponent_detected:
            # Strategy against aggressive opponent: choose 1 to minimize their points
            return 1
        else:
            last_turn = turn_history[-1]
            last_action = last_turn.actions[your_number]
            opponent_last_action = last_turn.actions[1 - your_number]

            # Standard cooperative strategy when not facing aggression
            if opponent_last_action in [2, 3]:
                return 2 if last_action == 3 else 3
            else:
                # Respond with 2 if the opponent is being unpredictable but not overly aggressive
                return 2
