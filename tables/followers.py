import psycopg2 as dbapi2

from common import *

#adds follower relationship and returns followedId if doesn t exist or userId if already exists
def addFollows(userId, followedId):
    with db() as connection:
        with connection.cursor() as cursor:
            checkQuery = """SELECT * FROM followers  WHERE follower = %s AND followed = %s"""
            addQuery = """INSERT INTO followers (follower, followed) values ( %(userId)s, %(followedId)s)"""
            try:
                if cursor.execute(checkQuery, userId, followedId) == None:
                    cursor.execute(addQuery, {'userId' : userId, 'followedId' : followedId })
                    return followedId
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return userId


def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS followers""")
                cursor.execute("""CREATE TABLE followers (follower INTEGER REFERENCES users(id),
                    followed INTEGER REFERENCES users(id)), UNIQUE(follower, followed)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return