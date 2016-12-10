import psycopg2 as dbapi2

from common import *

def addUser(name, mail, password):
    id = None
    with db() as connection:
        with connection.cursor() as cursor:
            query = """INSERT INTO users (name, mail, password) VALUES(%s, %s, %s) RETURNING id"""
            try:
                cursor.execute(query, [name, mail, password])
                id = cursor.fetchone()[0]
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return id;

def getUser(mail, password):
    user = None
    with db() as connection:
        with connection.cursor() as cursor:
            query = """SELECT * FROM users WHERE mail = %s AND password = %s"""
            try:
                cursor.execute(query, [mail, password])
                user = cursor.fetchone()
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return user

def getUserFromId(id):
    user = None
    with db() as connection:
        with connection.cursor() as cursor:
            query = """SELECT * FROM users WHERE id = %s"""
            try:
                cursor.execute(query, [id])
                user = cursor.fetchone()
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return user

