import random

from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult


class Practic(Player):
    name = "Practic"


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
        if not turn_history:
            return random.choice([2, 3])

        opponent_actions = [turn.actions[1 - your_number] for turn in turn_history]
        opponent_most_common_action = max(set(opponent_actions), key=opponent_actions.count)

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


























































































































































