#!/usr/bin/python

import sqlite3

def create_database():
    con = sqlite3.connect('pingpong.db')

    con.execute(
        """CREATE TABLE player (
           short_name TEXT PRIMARY KEY,
           name TEXT,
           rating REAL)
        """)

    con.execute(
        """CREATE TABLE match (
           player_a TEXT,
           player_b TEXT,
           score_a INTEGER,
           score_b INTEGER,
           elo_won_a REAL,
           elo_won_b REAL,
           date TEXT,
           FOREIGN KEY (player_a) REFERENCES players(short_name),
           FOREIGN KEY (player_b) REFERENCES players(short_name)
           )
        """) 
if __name__ == "__main__":
    create_database()
