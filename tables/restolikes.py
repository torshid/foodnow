import psycopg2 as dbapi2

from common import *

#adds restaurants likes by users and returns restoId if no such relation exists or user id if a like exists
def likeResto(userId, restoId):
    with db() as connection:
        with connection.cursor() as cursor:
            checkQuery = """SELECT * FROM restolikes  WHERE userId = %s AND restoId = %s"""
            addQuery = """INSERT INTO restoLikes (userId, restoId) values ( %(userId)s, %(restoId)s)"""
            try:
                if cursor.execute(checkQuery, userId, restoId) == None:
                    cursor.execute(addQuery, {'userId' : userId, 'restoId' : restoId })
                    return restoId
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return userId


def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS restolikes""")
                cursor.execute("""CREATE TABLE restolikes (userId INTEGER  users(id),
                    restoId INTEGER REFERENCES restos(id)), UNIQUE(userId, restoId)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return