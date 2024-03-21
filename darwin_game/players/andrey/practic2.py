import random
from collections import Counter

from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Practic2(Player):
    name = "Practic2"

    """
        
    ___________.__    .__         .__               ___.    _____                     __  .__               
    \__    ___/|  |__ |__| ______ |__| ______   ____\_ |___/ ____\_ __   ____ _____ _/  |_|__| ____   ____  
    |    |   |  |  \|  |/  ___/ |  |/  ___/  /  _ \| __ \   __\  |  \_/ ___\\__  \\   __\  |/  _ \ /    \ 
    |    |   |   Y  \  |\___ \  |  |\___ \  (  <_> ) \_\ \  | |  |  /\  \___ / __ \|  | |  (  <_> )   |  \
    |____|   |___|  /__/____  > |__/____  >  \____/|___  /__| |____/  \___  >____  /__| |__|\____/|___|  /
                    \/        \/          \/             \/                 \/     \/                    \/ 
        in case you don't wanna see the code








































































































    """

    @staticmethod
    def make_turn(turn_history: list[TurnResult], your_number: PlayerNumber) -> Action:
        def most_common_action(actions: list[Action]) -> Action:
            """Return the most common action from a list of actions. In case of a tie, the first action is returned."""
            counts = Counter(actions)
            most_common_element, _ = counts.most_common(1)[0]
            return most_common_element

        turn_num = len(turn_history)

        # If it's the first turn, return a random action
        if turn_num == 0:
            return random.choice([2, 3])

        # Detect if we're in a start deadlock (both players played the same action in all turns so far)
        if all(turn.actions[0] == turn.actions[1] for turn in turn_history):
            return random.choice([2, 3])

        # Cooperate if opponent cooperated in the last turn and we profited from it
        if turn_history[-1].actions[your_number] == 3 and turn_history[-1].actions[1 - your_number] == 2:
            logger.debug("Cooperate if opponent cooperated in the last turn and we profited from it")
            return 2

        # Expecting reciprocal cooperation for 2-3 alternation
        # If we cooperated and the opponent profited, it's our turn to profit
        if turn_history[-1].actions[1 - your_number] == 3 and turn_history[-1].actions[your_number] == 2:
            # Calculate how many turns since we're out of start deadlock
            for i, turn_result in enumerate(turn_history):
                if turn_result.actions[0] != turn_result.actions[1]:
                    break
            turns_since_non_identical_action = turn_num - i
            # If we're just out of start deadlock, give the opponent a chance to cooperate
            if turns_since_non_identical_action < 5:
                logger.debug("If we're just out of start deadlock")
                return 3

        cooperation_evaluation_length = 6
        # Calculate how cooperative the opponent was for the last cooperation_evaluation_length turns
        opponent_actions = [turn.actions[1 - your_number] for turn in turn_history[-cooperation_evaluation_length:]]
        opponent_cooperated_times = sum(1 for action in opponent_actions if action in [0, 1, 2])
        # If the opponent was cooperative enough, we expect them to cooperate
        if opponent_cooperated_times >= cooperation_evaluation_length / 2:
            logger.debug("If the opponent was cooperative enough, we expect them to cooperate")
            return 5 - most_common_action(opponent_actions)
        # If the opponent was not cooperative enough
        else:
            # Does opponent change their action?
            if len(set(opponent_actions)) > 1:
                logger.debug("The opponent was not cooperative enough, and changes their action")
                # We assume they are smart enough to change their action
                return 3

        opponent_actions = [turn.actions[1 - your_number] for turn in turn_history]
        opponent_most_common_action = most_common_action(opponent_actions)

        if opponent_most_common_action == 3:
            return 2
        elif opponent_most_common_action == 2:
            return 3
        elif opponent_most_common_action == 1:
            return 4
        elif opponent_most_common_action == 4:
            return 3
        else:
            return 5












































































"""boop"""