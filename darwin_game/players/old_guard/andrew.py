import random

from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult


class Andrew(Player):
    name = "Andrew"

    @staticmethod
    def make_turn(turn_history: list[TurnResult], your_number: PlayerNumber) -> Action:
        if not turn_history:
            return 5
        if turn_history[0].actions[1 - your_number] == 5:
            my_previous_turn, his_previous_turn = (
                turn_history[-1].actions[your_number],
                turn_history[-1].actions[1 - your_number],
            )
            if my_previous_turn == his_previous_turn:
                random.choice([2, 3])
            return his_previous_turn
        return 3
