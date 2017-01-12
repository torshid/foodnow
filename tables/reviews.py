import psycopg2 as dbapi2

from common import *


def getUserReviews(userId):
    list = []
    with db() as connection:
        with connection.cursor() as cursor:
            query = """SELECT * FROM reviews WHERE user_id = %(userId)s"""
            try:
                cursor.execute(query, {'userId': userId})
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
                cursor.execute("""CREATE TABLE reviews (id SERIAL PRIMARY KEY, user_id INTEGER ,
                resto_id INTEGER, dish_id INTEGER, content VARCHAR)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()


    addReview(1, 1, 1, "Nice food here!......")
    addReview(1, 1, 1, "These guys make really nice pizza!......")
    addReview(1, 1, 1, "So tasty, this kebap......")
    addReview(2, 1, 1, "Nice food here!......")
    addReview(2, 1, 1, "These guys make really nice pizza!......")
    addReview(2, 1, 1, "So tasty, this kebap......")
    addReview(3, 1, 1, "Nice food here!......")
    addReview(3, 1, 1, "These guys make really nice pizza!......")
    addReview(3, 1, 1, "So tasty, this kebap......")
    return

def getRestoReviews(restoId):
    list = []
    query = """SELECT content FROM dishes WHERE resto_id= %(restoId)s"""
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, {'restoId': restoId})
                list = cursor.fetchall()
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return list

def getDishReviews(dishId):
    list = []
    query = """SELECT content FROM dishes WHERE dish_id= %(dishId)s"""
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, {'dishId':dishId})
                list = cursor.fetchall()
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return list

def addReview(userId, restoId, dishId, content):
    if restoId is None:
        restoId = 0
    if dishId is None:
        dishId = 0
    if content is None or not userId:
        return False
    res = insert('reviews', {'user_id': userId, 'resto_id': restoId, 'dish_id' : dishId, 'content': content})
    return res

def deleteReview(id):
    deleted = False
    query = """DELETE FROM reviews WHERE id= %(id)s"""
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, {'id': id})
                deleted = True
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return      deleted

def getAllReviews(userId):
    list = []
    list = getUserReviews(userId)
    return list