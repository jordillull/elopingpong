#!/usr/bin/python 

N_SAMPLE_MATCHES = 1000
N_SAMPLE_PLAYERS = 12

from create_database import create_database 
from add_player      import add_player 
from add_match       import add_match

from random          import choice
from random          import randint

import string

def choice2(l):
    x = choice(l)
    l.remove(x)
    y = choice(l)
    l.append(x)
    return x,y
  

def make_samples():
    create_database()

    players = list(string.ascii_lowercase[0:N_SAMPLE_PLAYERS])
    for player in players:
        add_player(player, "Player {}".format(player.upper()))

    for i in range(N_SAMPLE_MATCHES):
        player_a, player_b = choice2(players)
        score_a = 21
        score_b = randint(0,19)

        add_match(player_a, score_a, player_b, score_b, False) 


if __name__ == "__main__":
    make_samples()
