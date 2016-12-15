import psycopg2 as dbapi2

from common import *

def addUser(name, mail, password):
    return insert('users', { 'name' : name, 'mail' : mail, 'password' : password })

def getUser(mail, password):
    return selectone('users', { 'mail' : mail, 'password' : password })

def getUserFromId(id):
    return selectone('users', { 'id' : id })

def getUserFromMail(mail):
    return selectone('users', { 'mail' : mail })

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS users""")
                cursor.execute("""CREATE TABLE users (id SERIAL, name VARCHAR, mail VARCHAR UNIQUE, password VARCHAR)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return

