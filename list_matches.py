#!/usr/bin/python

import sqlite3

def list_players():
    con = sqlite3.connect('pingpong.db') 
    cur = con.cursor() 

    for row in cur.execute("SELECT * FROM match ORDER BY date"):
        print row

    cur.close()
    con.close()

if __name__ == "__main__":
    list_players()
