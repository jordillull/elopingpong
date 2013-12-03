#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def count_matches(con, short_name):
    clean_match_table = """
     (
         SELECT player_a as player,
                player_b as opponent,
                score_a as player_score,
                score_b as opponent_score
           FROM match
          WHERE player_a = '{SHORT_NAME}'
     UNION
          SELECT player_b as player,
                 player_a as opponent,
                 score_b as player_score,
                 score_a as opponent_score
            FROM match where player_b = '{SHORT_NAME}'
     )
    """.format(SHORT_NAME=short_name);

    wins_query = """
        SELECT COUNT(*)
          FROM {TABLE}
         WHERE player_score > opponent_score""".format(TABLE=clean_match_table);

    losts_query = """
        SELECT COUNT(*)
          FROM {TABLE}
         WHERE player_score < opponent_score""".format(TABLE=clean_match_table);


    cur = con.cursor()
    cur.execute(wins_query);
    wins = cur.fetchone()[0];
    cur.close()

    cur = con.cursor()
    cur.execute(losts_query);
    losts = cur.fetchone()[0];
    cur.close()

    return (wins, losts)




def get_players():
    con = sqlite3.connect('pingpong.db')
    cur = con.cursor()

    query = """
        SELECT player.name,
               player.short_name,
               player.rating
          FROM player
      ORDER BY rating DESC"""
    cur.execute(query)

    players = [];
    for row in cur.fetchall():
        player = {'name' : row[0].encode('utf-8'), 'short_name' : row[1], 'rating': row[2] }

        player['wins'], player['losts'] =  count_matches(con, player['short_name'])
        players.append(player)


    cur.close()
    con.close()

    return players

def print_players(players):

    template = "{RATING:7} | {MATCHES:8} | {NAME:20}"
    header = template.format(NAME="Name", RATING="Rating", MATCHES="V - D")
    print header
    print '-' * len(header)

    template = "{RATING:n} | {MATCHES:8} | {NAME:20}"
    for player in players:
        print template.format(NAME=player['name'], RATING=player['rating'], MATCHES="{WINS:2} - {LOSTS:2}".format(WINS=player['wins'], LOSTS=player['losts']))



def list_players():
    players = get_players()
    print_players(players)

if __name__ == "__main__":
    list_players()
