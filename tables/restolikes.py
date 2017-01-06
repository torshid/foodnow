import psycopg2 as dbapi2

from common import *

#adds restaurants likes by users and returns restoId if no such relation exists or user id if a like exists
def likeResto(userId, restoId):
    liked = insert('restolikes', {'user_id': userId, 'resto_id': restoId})
    return liked

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
                cursor.execute("""CREATE TABLE restolikes (user_id INTEGER REFERENCES users(id),
                    resto_id INTEGER REFERENCES restos(id)), UNIQUE(user_id, resto_id)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return