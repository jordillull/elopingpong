#!/usr/bin/python

MAX_ELO_GAIN = 32.0
DEBUG = False

def compute_new_ratings(score_a, rating_a, score_b, rating_b):

    if score_a > score_b: 
      # Player A Wins
      game_dominance_a = (((score_a * 2) + 15) - score_b)  / ((score_a * 2) + 15.0)
      game_dominance_b = 1 - game_dominance_a
    else:                
      # Player B Wins
      game_dominance_b = (((score_b * 2) + 15) - score_a)  / ((score_b * 2) + 15.0)
      game_dominance_a = 1 - game_dominance_b


    if DEBUG:
        print("Game dominance A {0}".format(game_dominance_a))
        print("Game dominance B {0}".format(game_dominance_b))

    expected_a = rating_a / ((rating_a + rating_b) * 1.0)
    expected_b = 1 - expected_a 

    if DEBUG:
        print("Expected A {0}".format(expected_a))
        print("Expected B {0}".format(expected_b))

    new_rating_a = rating_a + (MAX_ELO_GAIN * ( game_dominance_a - expected_a))
    new_rating_b = rating_b + (MAX_ELO_GAIN * ( game_dominance_b - expected_b))

    return [new_rating_a, new_rating_b]

