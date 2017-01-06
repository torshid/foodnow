import psycopg2 as dbapi2

from common import *

def likeDish(userId, dishId):
    with db() as connection:
        with connection.cursor() as cursor:
            result = 0
            query = """INSERT INTO dishlikes values (%s, %s)"""
            try:
                if likesDish(userId, dishId):
                    result = 1
                else :
                    cursor.execute(query, (userId, dishId))
                    result = 2
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return result



def likesDish(userId, dishId):
    liked = False
    with db() as connection:
        with connection.cursor() as cursor:
            countQuery = """SELECT * FROM dishlikes  WHERE user_id = %s AND dish_id = %s"""
            try:
                cursor.execute(countQuery, (userId, dishId))
                result = cursor.fetchone();
                if result:
                    liked = True
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return liked

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

def getUserLikedDishesId(userId):
    list = []
    dishlist = selectall('dishlikes', {'user_id' : userId});
    if dishlist:
        for dish in dishlist:
            list.append(dish[1])
    return list

def getLikedDishes(userId):
    list = []
    list = selectall('dishlikes', {'user_id': userId})
    return list


def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS dishlikes""")
                cursor.execute("""CREATE TABLE dishlikes (user_id INTEGER,
                    dish_id INTEGER)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
            likeDish(1, 1)
            likeDish(3, 1)
    return