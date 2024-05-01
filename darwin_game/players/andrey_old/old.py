from darwin_game.models.player import Action, Player, PlayerNumber, TurnResult

import logging

import numpy as np


class OldAndrey(Player):
    name = "OldAndrey"

    @staticmethod
    def make_turn(turn_history: list[TurnResult], your_number: PlayerNumber) -> Action:
        def antideadlock():
            rnd = np.random.uniform(0, 1)
            if rnd <= 0.12:
                return 1
            if rnd <= 0.6:
                return 2
            return 3

        turn_num = len(turn_history) + 1

        if turn_num == 1:
            return antideadlock()

        friend_previous_turn = turn_history[-1].actions[1 - your_number]
        our_previous_turn = turn_history[-1].actions[your_number]
        opponent_points = sum(turn.results[1 - your_number] for turn in turn_history)
        our_points = sum(turn.results[your_number] for turn in turn_history)

        threshold = 5
        if turn_num > threshold:
            opponent_is_superior = False
            if turn_num > threshold * 2 and opponent_points > our_points + 3:
                opponent_is_superior = True

            if opponent_is_superior:
                if opponent_points - our_points > 5:
                    return 5
                return opponent_points - our_points

        for turn in turn_history:
            if turn.actions[0] != turn.actions[1]:
                break
        else:
            return antideadlock()

        if friend_previous_turn == our_previous_turn:
            if opponent_points > our_points:
                return 3
            if opponent_points < our_points:
                return 2
            if turn_num > threshold * 2:
                return 3  # something's fishy, opponent doesn't cooperate in the expected way

        if opponent_points > our_points:
            return 3
        if opponent_points < our_points:
            return 2
        if opponent_points == our_points:
            if our_previous_turn == 2:
                return 3
            if our_previous_turn == 3:
                return 2

        return antideadlock()


# def predict_randomness_efficient(opponent_turns):
#     # Define the subsets of interest
#     subsets = {
#         '(1, 2, 3)': set([1, 2, 3]),
#         '(2, 3)': set([2, 3]),
#         '(1, 2, 3, 4, 5)': set([1, 2, 3, 4, 5]),
#         '(3, 4, 5)': set([3, 4, 5])
#     }

#     # Calculate observed frequencies for each possible turn (0-5)
#     observed_freq = [opponent_turns.count(i) for i in range(6)]

#     # Prepare a dictionary to hold deviation scores for each subset
#     deviation_scores = {}

#     for subset_label, subset_numbers in subsets.items():
#         # Calculate the total number of turns that fall within the subset
#         total_subset_turns = sum(observed_freq[i] for i in subset_numbers)

#         # The expected frequency for each turn in the subset, if randomly distributed
#         expected_freq_per_turn = total_subset_turns / len(subset_numbers)

#         # Calculate the deviation score as the sum of absolute differences
#         # between observed and expected frequencies for turns in the subset
#         deviation_score = sum(abs(observed_freq[i] - expected_freq_per_turn) for i in subset_numbers)

#         # Normalize the deviation score by the total number of turns
#         if total_subset_turns > 0:
#             deviation_scores[subset_label] = deviation_score / total_subset_turns
#         else:
#             deviation_scores[subset_label] = float('inf')  # Impossibly high score if no turns fall within the subset

#     # Return the subset with the minimum deviation score
#     min_deviation_subset = min(deviation_scores, key=deviation_scores.get)
#     return min_deviation_subset, deviation_scores

# # Example usage with a hypothetical set of turns
# predict_randomness_efficient(example_turns)


"""boop"""
