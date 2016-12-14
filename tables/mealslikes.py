import psycopg2 as dbapi2

from common import *

#TODO needs to be modified
def likeMeal(userId, restoId):
    with db() as connection:
        with connection.cursor() as cursor:
            checkQuery = """SELECT * FROM restolikes  WHERE user_id = %s AND resto_id = %s"""
            addQuery = """INSERT INTO restoLikes (user_id, resto_id) values ( %(userId)s, %(restoId)s)"""
            try:
                if cursor.execute(checkQuery, userId, restoId) == None:
                    cursor.execute(addQuery, {'userId' : userId, 'restoId' : restoId })
                    return restoId
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return userId;

def getTotalLikesMeals(userId):
    with db() as connection:
        with connection.cursor() as cursor:
            countQuery = """SELECT COUNT(resto_id) FROM mealslikes  WHERE user_id = %s"""
            try:
                cursor.execute(countQuery, userId)
                result = cursor.fetchone();
                mCount = result[0]
                return mCount
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return 0;


def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS restolikes""")
                cursor.execute("""CREATE TABLE restolikes (user_id INTEGER  users(id),
                    resto_id INTEGER REFERENCES restos(id)), UNIQUE(user_id, resto_id)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return