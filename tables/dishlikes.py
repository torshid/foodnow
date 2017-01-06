import psycopg2 as dbapi2

from common import *

def likeDish(userId, dishId):
    liked = False
    with db() as connection:
        with connection.cursor() as cursor:
            addQuery = """INSERT INTO restoLikes (user_id, resto_id) values ( %s, %s)"""
            try:
                if not likes(userId, dishId):
                    cursor.execute(addQuery, (userId, dishId ))
                    liked = True
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return      False

def likes(userId, dishId):
    result = selectall('dishlikes', {'user_id': userId, 'dish_id': dishId})
    if result:
        return True
    return False

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
    with db() as connection:
        with connection.cursor() as cursor:
            query = """SELECT dish_id FROM dishlikes  WHERE user_id = %(userId)s"""
            try:
                cursor.execute(query)
                list = cursor.fetchall();
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    #selectall('dishlikes', {'user_id': userId});
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
            likeDish(1, 1)
            likeDish(3, 1)
    return