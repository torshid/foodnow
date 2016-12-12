import psycopg2 as dbapi2

from common import *

def addEmployee(restoid, userid, role):
    return insert('employees', { 'restoid' : restoid, 'userid' : userid, 'role' : role })

def deleteEmployee(id):
    return delete('employees', { 'id' : id })

def getRestoEmployees(restoid):
    return selectall('users', { 'restoid' : restoid })

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS employees""")
                cursor.execute("""CREATE TABLE users (id SERIAL, restoid INTEGER, userid INTEGER, role SMALLINT)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return
