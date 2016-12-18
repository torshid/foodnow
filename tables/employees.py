import psycopg2 as dbapi2

from common import *

def addEmployee(restoid, userid, role):
    return insert('employees', { 'restoid' : restoid, 'userid' : userid, 'role' : role })

def deleteEmployee(id):
    return delete('employees', { 'id' : id })

def getRestoEmployees(restoid):
    return selectall('employees', { 'restoid' : restoid })

def getUserEmployments(userid):
    return selectall('employees', { 'userid' : userid })

def getUserRestoEmployment(restoid, userid):
    return selectone('employees', { 'restoid' : restoid, 'userid' : userid })

def isManager(employee):
    return isRole(employee, rolemanager)

def isWorker(employee):
    return isRole(employee, roleworker)

def isRole(employee, role):
    return employee != None and employee[3] == role

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS employees""")
                cursor.execute("""CREATE TABLE employees (id SERIAL, restoid INTEGER, userid INTEGER, role SMALLINT)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return
