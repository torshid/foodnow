import psycopg2 as dbapi2

from common import *

def addEmployee(restoid, userid, role):
    return insert('employees', { 'restoid' : restoid, 'userid' : userid, 'role' : role })

def getEmployee(id):
    return selectone('employees', { 'id' : id }, 'ORDER BY id DESC')

def deleteEmployee(id):
    return update('employees', { 'deleted' : '1' }, { 'id' : id })
    # return delete('employees', { 'id' : id })

def getRestoEmployees(restoid):
    return selectall('employees', { 'restoid' : restoid, 'deleted' : '0' })

def getUserEmployments(userid):
    return selectall('employees', { 'userid' : userid, 'deleted' : '0' })

def getUserRestoEmployment(restoid, userid):
    return selectone('employees', { 'restoid' : restoid, 'userid' : userid, 'deleted' : '0' })

def isManager(employee):
    return isRole(employee, rolemanager)

def isWorker(employee):
    return isRole(employee, roleworker)

def isDriver(employee):
    return isRole(employee, roledriver)

def isRole(employee, role):
    if not isinstance(employee, tuple):
        employee = (0, 0, 0, employee, 0)
    return employee != None and employee[3] == role

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS employees""")
                cursor.execute("""CREATE TABLE employees (id SERIAL, restoid INTEGER, userid INTEGER, role SMALLINT, deleted BOOLEAN DEFAULT false)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return
