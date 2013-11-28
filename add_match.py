#!/usr/bin/python



import sqlite3

import sys

import elo

import datetime



DEFAULT_RATING = 1500



def get_rating(con, player):

    cur = con.cursor()

    rating = cur.execute("""

        SELECT rating 

          FROM player

         WHERE short_name = '{0}'""".format(player)).fetchone()



    return float(rating[0])



def log_match_info(player_a, score_a, player_b, score_b, rating_a, rating_b, new_rating_a, new_rating_b):

    print "{0} won the Match! {1} - {2}".format(player_a if score_a > score_b else player_b, score_a, score_b)

    print 

    print "{0} {1} {2:.2f} points. His new rating is {3:.2f}".format(player_a, 'won' if new_rating_a > rating_a else 'lost', abs(new_rating_a-rating_a), new_rating_a)

    print

    print "{0} {1} {2:.2f} points. His new rating is {3:.2f}".format(player_b, 'won' if new_rating_b > rating_b else 'lost', abs(new_rating_b-rating_b), new_rating_b) 



def add_match(player_a, score_a, player_b, score_b):

    con = sqlite3.connect('pingpong.db') 

    cur = con.cursor() 



    rating_a = get_rating(con, player_a)

    rating_b = get_rating(con, player_b)



    if not rating_a:

        print "Error: Rating for player {0} was not found".format(player_a)

        return



    if not rating_b:

        print "Error: Rating for player {0} was not found".format(player_b)

        return

    

    new_rating_a, new_rating_b = elo.compute_new_ratings(score_a, rating_a, score_b, rating_b)



    query = """

         INSERT INTO match 

             (player_a, player_b, score_a, score_b, elo_won_a, elo_won_b, date) 

         VALUES ('{0}','{1}','{2}','{3}','{4}','{5}', '{6}')

            """.format(

                player_a, player_b, 

                score_a, score_b, 

                new_rating_a - rating_a,

                new_rating_b - rating_b,

                str(datetime.datetime.now())

                ) 

    cur.execute(query) 



    query = """

        UPDATE player

           SET rating = {0}

         WHERE short_name = '{1}'"""



    cur.execute(query.format(new_rating_a, player_a))

    cur.execute(query.format(new_rating_b, player_b))



    log_match_info(player_a, score_a, player_b, score_b, rating_a, rating_b, new_rating_a, new_rating_b)



    con.commit() 

    cur.close()

    con.close()



if __name__ == "__main__":

    if len(sys.argv) != 5:

        print "Incorrect number of parameters."

        print "  Usage: ./add_match player_a score_a player_b score_b"

    else:

        add_match(sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4]))
