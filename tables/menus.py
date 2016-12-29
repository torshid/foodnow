import psycopg2 as dbapi2

from common import *

def addMenu(restoid, name, disposition, visible):
    return insert('menus', { 'restoid' : restoid, 'name' : name, 'disposition' : disposition, 'visible' : visible})

def getRestoMenus(restoid):
    return selectall('menus', { 'restoid' : restoid }, 'ORDER BY disposition')

def getMenu(id):
    return selectone('menus', { 'id' : id })

def getRestoMenuHighestDisposition(restoid):
    return selectone('menus', { 'restoid' : restoid }, 'ORDER BY disposition DESC')

def updateMenu(id, name, disposition, visible):
    return update('menus', { 'name' : name, 'disposition' : disposition, 'visible' : visible}, { 'id' : id })

def deleteMenu(id):
    return delete('menus', { 'id' : id })

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS menus""")
                cursor.execute("""CREATE TABLE menus (id SERIAL, restoid INTEGER, name VARCHAR, disposition SMALLINT, visible BOOLEAN)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return
