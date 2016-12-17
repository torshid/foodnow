import psycopg2 as dbapi2

from common import *

def addMenu(restoid, name, disposition, visible):
    return insert('menus', { 'restoid' : restoid, 'name' : pseudo, 'disposition' : disposition, 'visible' : visible})

def getRestoMenus(restoid):
    return selectall('menus', { 'restoid' : restoid }, 'ORDER BY disposition')

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS menus""")
                cursor.execute("""CREATE TABLE menus (id SERIAL, restoid INTEGER, name VARCHAR, disposition INTEGER, visible BOOLEAN)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return
