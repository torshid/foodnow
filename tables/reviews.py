import psycopg2 as dbapi2

from common import *

import psycopg2 as dbapi2

from common import *

#need to add mealId
def review(userId, restoId, content):
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                insert('reviews', {'user_id' : userId, 'resto_id' : restoId, 'content' : 'content'})
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return


def getUserReviews(userId):
    list = []
    with db() as connection:
        with connection.cursor() as cursor:
            query = """"SELECT * FROM reviews WHERE user_id = %s"""
            try:
                cursor.execute(query, userId)
                list = cursor.fetchall();
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return list


def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS restorecommendations""")
                cursor.execute("""CREATE TABLE restorecommendations (user_id INTEGER REFERENCES users(id),
                resto_id REFERENCES restos(id), content VARCHAR)""")
                #cursor.execute("""DROP TABLE IF EXISTS foodrecommendations""")
                #cursor.execute("""CREATE TABLE foodrecommendations (recommender_id INTEGER REFERENCES users(id), meal_id INTEGER REFERENCES  content VARCHAR)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return
