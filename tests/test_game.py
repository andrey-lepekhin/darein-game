from unittest.mock import Mock

from darwin_game.core.game import Game
from darwin_game.models.player import Player


class MockPlayer(Player):
    def make_turn(self, turn_results):
        # Implement a simple logic or return a fixed action
        return 0

    name = "MockPlayer"


def test_get_turn_result():
    player1 = MockPlayer()
    player2 = MockPlayer()
    game = Game(player1, player2, max_turns=1)

    action1 = 3
    action2 = 2
    result = game._get_turn_result(player1_action=action1, player2_action=action2)
    assert result.player1_reward == 3
    assert result.player2_reward == 2

    action1 = 4
    action2 = 2
    result = game._get_turn_result(player1_action=action1, player2_action=action2)
    assert result.player1_reward == 0
    assert result.player2_reward == 0


def test_play_turn():
    player1 = MockPlayer()
    player2 = MockPlayer()
    player1.make_turn = Mock(return_value=1)
    player2.make_turn = Mock(return_value=2)
    game = Game(player1, player2, max_turns=1)

    game._play_turn()
    assert len(game.turn_history) == 1
    assert game.turn_number == 1


def test_play_game():
    player1 = MockPlayer()
    player2 = MockPlayer()
    player1.make_turn = Mock(return_value=1)
    player2.make_turn = Mock(return_value=2)
    game = Game(player1, player2, max_turns=2)

    results = game.play_game()
    assert game.turn_number == 2
    assert results[player1] == 2
    assert results[player2] == 4

    player1.make_turn = Mock(return_value=5)
    player2.make_turn = Mock(return_value=5)
    game = Game(player1, player2, max_turns=2)

    results = game.play_game()
    assert results[player1] == 0
    assert results[player2] == 0
