import psycopg2 as dbapi2

from common import *

def likeDish(userId, dishId):
    liked = False
    with db() as connection:
        with connection.cursor() as cursor:
            checkQuery = """SELECT * FROM dishlikes  WHERE user_id = %s AND dish_id = %s"""
            addQuery = """INSERT INTO restoLikes (user_id, resto_id) values ( %(userId)s, %(dishId)s)"""
            try:
                if cursor.execute(checkQuery, (userId, dishId)) == None:
                    cursor.execute(addQuery, {'userId' : userId, 'dishId' : dishId })
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return

def getTotalLikesDish(dishId):
    mCount = 0
    with db() as connection:
        with connection.cursor() as cursor:
            countQuery = """SELECT COUNT(user_id) FROM dishlikes  WHERE dish_id = %s"""
            try:
                cursor.execute(countQuery, dishId)
                result = cursor.fetchone();
                mCount = result[0]
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return mCount;

def getLikedDishes(userId):
    list = []
    selectall('dishlikes', {'user_id': userId});
    return list


def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS dishlikes""")
                cursor.execute("""CREATE TABLE dishlikes (user_id INTEGER REFERENCES users(id),
                    dish_id INTEGER REFERENCES dishes(id)), UNIQUE(user_id, dish_id)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return