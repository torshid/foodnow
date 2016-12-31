import psycopg2 as dbapi2

from common import *

def addDish(menuid, name, price, disposition, visible):
    return insert('dishes', { 'menuid' : menuid, 'name' : name, 'price' : price, 'disposition' : disposition, 'visible' : visible})

def getDish(id):
    return selectone('dishes', { 'id' : id })

def deleteDish(id):
    return delete('dishes', { 'id' : id })

def getMenuDishes(menuid):
    return selectall('dishes', { 'menuid' : menuid }, 'ORDER BY disposition')

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS dishes""")
                cursor.execute("""CREATE TABLE dishes (id SERIAL, menuid INTEGER, name VARCHAR, price REAL, disposition SMALLINT, visible BOOLEAN)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return