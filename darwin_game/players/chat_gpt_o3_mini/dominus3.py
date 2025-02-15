from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult
import random

class DominusV3(Player):
    name = "DominusV3"

    @staticmethod
    def make_turn(turn_history: list[TurnResult], your_number: PlayerNumber) -> Action:
        opponent = 1 - your_number
        # Fixed cooperative signal for the first three turns.
        signal = [2, 3, 2]
        if len(turn_history) < 3:
            return signal[len(turn_history)]

        # Detect Rocket-like behavior: opponent's first three moves equal our signal.
        opp_initial = [turn.actions[opponent] for turn in turn_history[:3]]
        rocket_mode = (opp_initial == signal)
        
        # Compute cumulative scores.
        my_score = sum(turn.results[your_number] for turn in turn_history)
        opp_score = sum(turn.results[opponent] for turn in turn_history)

        # Analyze opponent's overall use of cooperative moves.
        opp_moves = [turn.actions[opponent] for turn in turn_history]
        count2 = opp_moves.count(2)
        count3 = opp_moves.count(3)
        exploitation = False
        # If opponent favors 2 or if we are trailing, prepare to exploit.
        if count2 > count3 or (opp_score - my_score >= 2):
            exploitation = True

        # --- Rocket mode adaptation ---
        if rocket_mode:
            last_turn = turn_history[-1]
            my_last = last_turn.actions[your_number]
            opp_last = last_turn.actions[opponent]
            # If last round was perfect cooperation (sum==5), deliberately repeat our move
            # to break Rocket's alternating lock.
            if my_last + opp_last == 5:
                return my_last
            else:
                # Otherwise, mostly play 3 to push for a 3–2 split;
                # occasionally mix in a 2 to introduce variation.
                return 3 if random.random() < 0.8 else 2

        # --- Non-Rocket opponents ---
        # If exploitation conditions are met, always play 3.
        if exploitation:
            return 3

        # Otherwise, try to maintain mutual cooperation.
        last_turn = turn_history[-1]
        my_last = last_turn.actions[your_number]
        opp_last = last_turn.actions[opponent]
        if my_last + opp_last == 5:
            # Alternate: if our last move was 2, now play 3; if 3, then play 2.
            return 3 if my_last == 2 else 2

        # If the cooperative pattern broke, mimic the opponent’s last cooperative move.
        if opp_last in [2, 3]:
            return opp_last
        
        # Default fallback.
        return random.choice([2, 3])
