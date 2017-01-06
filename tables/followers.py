import psycopg2 as dbapi2

from common import *

#adds follower relationship and returns followedId if doesn t exist or userId if already exists
def addFollows(userId, followedId):
    with db() as connection:
        with connection.cursor() as cursor:
            result = 0
            query = """INSERT INTO followers(follower, followed) values (%s, %s)"""
            try:
                if likesResto(userId, followedId):
                    result = 1
                else :
                    cursor.execute(query, (userId, followedId))
                    result = 2
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return result


def follows(follower, followed):
    result = selectone('followers', {'follower': follower, 'followed': followed})
    if result:
        return True
    return False

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS followers""")
                cursor.execute("""CREATE TABLE followers (follower INTEGER ,
                    followed INTEGER)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return

def getFollowedList(usedId): #people the user follows
    list = []
    list = selectall('followers', {'follower': userId})
    return list

def getFollowersList(usedId): #people who follow the user
    list = []
    list = selectall('followers', {'followed': userId})
    return list