import psycopg2 as dbapi2

from common import *

def addDish(menuid, name, price, disposition, visible, description):
    return insert('dishes', { 'menuid' : menuid, 'name' : name, 'price' : price, 'disposition' : disposition, 'visible' : visible, 'description' : description })

def getDish(id):
    return selectone('dishes', { 'id' : id })

def getMenuDishesHighestDisposition(menuid):
    return selectone('dishes', { 'menuid' : menuid, 'deleted' : '0' }, 'ORDER BY disposition DESC')

def deleteDish(id):
    return update('dishes', { 'deleted' : '1' }, { 'id' : id })
    # return delete('dishes', { 'id' : id })

def getMenuDishes(menuid):
    return selectall('dishes', { 'menuid' : menuid, 'deleted' : '0' }, 'ORDER BY disposition')

def updateDish(id, menuid, name, price, disposition, visible, description):
    return update('dishes', { 'menuid' : menuid, 'name' : name, 'price' : price, 'disposition' : disposition, 'visible' : visible, 'description' : description }, { 'id' : id })

def countMenuDishes(menuid):
    return count('dishes', 'id', { 'menuid' : menuid, 'deleted' : '0' })

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS dishes""")
                cursor.execute("""CREATE TABLE dishes (id SERIAL, menuid INTEGER, name VARCHAR, price REAL, disposition SMALLINT, visible BOOLEAN, deleted BOOLEAN DEFAULT false, description VARCHAR DEFAULT '')""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return

def getMostLikedDishes(): #incomplete
    list = []
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""SELECT * FROM dishes LIMIT 10""")
                list = cursor.fetchall();
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return      list