import psycopg2 as dbapi2

from common import *

def addResto(name, pseudo, mail, phone):
    id = None
    with db() as connection:
        with connection.cursor() as cursor:
            query = """INSERT INTO restos (name, pseudo, mail, phone) VALUES(%s, %s, %s, %s) RETURNING id"""
            try:
                cursor.execute(query, [name, pseudo, mail, phone])
                id = cursor.fetchone()[0]
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return id

def getResto(pseudo):
    user = None
    with db() as connection:
        with connection.cursor() as cursor:
            query = """SELECT * FROM restos WHERE pseudo = %s"""
            try:
                cursor.execute(query, [pseudo])
                user = cursor.fetchone()
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return user

def getRestoFromId(id):
    user = None
    with db() as connection:
        with connection.cursor() as cursor:
            query = """SELECT * FROM restos WHERE id = %s"""
            try:
                cursor.execute(query, [id])
                user = cursor.fetchone()
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return user


