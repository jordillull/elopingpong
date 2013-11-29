#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def get_players():
    con = sqlite3.connect('pingpong.db')
    cur = con.cursor()

    query = """
        SELECT player.name,
               (SELECT count(*)
                  FROM match
                 WHERE player_a = short_name
                    OR player_b = short_name
              ),
              player.rating
         FROM player
     ORDER BY rating DESC"""

    cur.execute(query)

    players = cur.fetchall()

    cur.close()
    con.close()

    return players

def print_players(players):

    template = "{NAME:20} | {MATCHES:8} | {RATING:8}"
    header = template.format(NAME="Name", MATCHES="Matches", RATING="Rating")
    print header
    print '-' * len(header)

    template = "{NAME:20} | {MATCHES:8} | {RATING:n}"
    for row in players:
        print template.format(NAME=row[0].encode('utf-8'), MATCHES=row[1], RATING=row[2])



def list_players():
    players = get_players()
    print_players(players)

if __name__ == "__main__":
    list_players()
