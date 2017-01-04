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
                cursor.execute("""DROP TABLE IF EXISTS reviews""")
                cursor.execute("""CREATE TABLE reviews (user_id INTEGER REFERENCES users(id),
                resto_id REFERENCES restos(id), dish_id REFERENCES dishes(id), content VARCHAR)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return

def getRestoReviews(restoId):
    list = []
    query = """SELECT content FROM dishes WHERE resto_id= %s"""
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, [restoId])
                list = cursor.fetchall()
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return list

def getDishReviews(dishId):
    list = []
    query = """SELECT content FROM dishes WHERE dish_id= %s"""
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, [dishId])
                list = cursor.fetchall()
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return list
