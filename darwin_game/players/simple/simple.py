import random

from darwin_game.models.player import Player


class P1(Player):
    name = "Always zero"

    @staticmethod
    def make_turn(turn_history, your_number):
        return 0


class P2(Player):
    name = "Always one"

    @staticmethod
    def make_turn(turn_history, your_number):
        return 1


class P3(Player):
    name = "2 or 3"

    @staticmethod
    def make_turn(turn_history, your_number):
        # random int 2 or 3

        return random.choice([2, 3])


class P4(Player):
    name = "Always 3"

    @staticmethod
    def make_turn(turn_history, your_number):
        return 3


class P5(Player):
    name = "Mirrors opponent's action"

    @staticmethod
    def make_turn(turn_history, your_number):
        if not turn_history:
            return random.choice([2, 3])
        return turn_history[-1].actions[1 - your_number]


class P6(Player):
    name = "Random(1, 2, 3, 4, 5)"

    @staticmethod
    def make_turn(turn_history, your_number):
        return random.choice([1, 2, 3, 4, 5])


class P7(Player):
    name = "Always 4"

    @staticmethod
    def make_turn(turn_history, your_number):
        return 4


class P8(Player):
    name = "Always 5"

    @staticmethod
    def make_turn(turn_history, your_number):
        return 5


class P9(Player):
    name = "Random(3, 4, 5)"

    @staticmethod
    def make_turn(turn_history, your_number):
        return random.choice([3, 4, 5])


class P10(Player):
    name = "Random(2, 3, 4)"

    @staticmethod
    def make_turn(turn_history, your_number):
        return random.choice([2, 3, 4])


class P11(Player):
    name = "Random(1, 2, 3)"

    @staticmethod
    def make_turn(turn_history, your_number):
        return random.choice([1, 2, 3])
