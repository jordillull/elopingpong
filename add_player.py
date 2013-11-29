#!/usr/bin/python

import sqlite3
import sys

DEFAULT_RATING = 1500

def add_player(short_name, name):
    con = sqlite3.connect('pingpong.db') 
    cur = con.cursor()

    query = """INSERT INTO player VALUES ('{0}','{1}','{2}')""".format(short_name, name, DEFAULT_RATING)
    cur.execute(query) 

    con.commit() 
    cur.close()
    con.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Incorrect number of parameters."
        print "  Usage: ./add_player short_name long_name"
    else:
        add_player(sys.argv[1], sys.argv[2])
