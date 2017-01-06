import psycopg2 as dbapi2

from common import *

#adds restaurants likes by users and returns restoId if no such relation exists or user id if a like exists
def likeResto(userId, restoId):
    with db() as connection:
        with connection.cursor() as cursor:
            result = 0
            query = """INSERT INTO restolikes values (%s, %s)"""
            try:
                if likesResto(userId, restoId):
                    result = 1
                else :
                    cursor.execute(query, (userId, restoId))
                    result = 2
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return result

def getLikedRestoDetails(userId, restoId):
    with db() as connection:
        with connection.cursor() as cursor:
            result = None
            #checkQuery = """SELECT * FROM restolikes  WHERE userId = %s AND restoId = %s"""
            query = """SELECT DISTINCT restos.id, restos.name, restos.pseudo, restos.phone,
                restolikes.date FROM restolikes  restos WHERE users.user_id = %s AND resto.id = %s"""
            try:
                #if cursor.execute(checkQuery, userId, restoId) == None:
                #    return None
                if likesResto(userId, restoId):
                    cursor.execute(query,(userId, restoId) )
                result = cursor.fetchall();
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return  result

def getTotalLikesRestos(userId):
    with db() as connection:
        with connection.cursor() as cursor:
            countQuery = """SELECT COUNT(resto_id) FROM restolikes  WHERE user_id = %s"""
            try:
                cursor.execute(countQuery, userId)
                result = cursor.fetchone();
                rCount = result[0]
                return rCount
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return 0;

def likesResto(userId, restoId):
    liked = False
    with db() as connection:
        with connection.cursor() as cursor:
            countQuery = """SELECT * FROM restolikes  WHERE user_id = %s AND resto_id = %s"""
            try:
                cursor.execute(countQuery, (userId, restoId))
                result = cursor.fetchone();
                if result:
                    liked = True
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return liked

def getLikedRestos(userId):
    restolist = selectall("restolikes", {'user_id' : userId});
    result = []
    if restolist:
        for resto in restolist:
            element = getLikedRestoDetails(userId, resto[1])
            result.append(element)
    return result

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS restolikes""")
                cursor.execute("""CREATE TABLE restolikes (user_id INTEGER,
                    resto_id INTEGER)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return

def getUserLikedRestosId(userId):
    list = []
    restolist = selectall("restolikes", {'user_id' : userId});
    for resto in restolist:
        list.append(resto[1])
    return list