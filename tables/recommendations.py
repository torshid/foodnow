import psycopg2 as dbapi2

from common import *

def review(userId, restoId, content):
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                insert('recommendations', {'recommender_id' : userId, 'resto_id' : restoId, 'content' : 'content'})
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return


def getAll():
    list = []
    with db() as connection:
        with connection.cursor() as cursor:
            query = """"SELECT * FROM recommendations"""
            try:
                cursor.execute(query)
                list = cursor.fetchall();
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return list


def reset():
    from tables import reviews
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS restorecommendations""")
                cursor.execute("""CREATE TABLE restorecommendations (recommender_id INTEGER REFERENCES users(id),
                resto_id REFERENCES restos(id), content VARCHAR)""")
                #cursor.execute("""DROP TABLE IF EXISTS foodrecommendations""")
                #cursor.execute("""CREATE TABLE foodrecommendations (recommender_id INTEGER REFERENCES users(id), meal_id INTEGER REFERENCES  content VARCHAR)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()


    return
