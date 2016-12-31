import psycopg2 as dbapi2

from common import *

def addResto(name, pseudo, mail, phone, currency, description):
    return insert('restos', { 'name' : name, 'pseudo' : pseudo, 'mail' : mail, 'phone' : phone, 'currency' : currency, 'description' : description })

def getResto(pseudo):
    return selectone('restos', { 'pseudo' : pseudo })

def getRestoFromId(id):
    return selectone('restos', { 'id' : id })

def updateResto(id, name, pseudo, mail, phone, accessible, warnmsg, currency, description):
    return update('restos', { 'name' : name, 'pseudo' : pseudo, 'mail' : mail, 'phone' : phone, 'accessible' : accessible, 'warnmsg' : warnmsg, 'currency' : currency, 'description' : description }, { 'id' : id })

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS restos""")
                cursor.execute(("CREATE TABLE restos ("
                    "id SERIAL, name VARCHAR, pseudo VARCHAR UNIQUE, mail VARCHAR, phone VARCHAR,"
                    "accessible BOOLEAN DEFAULT false, warnmsg VARCHAR DEFAULT 'Our restaurant page is under construction, see you soon!',"
                    "currency VARCHAR, description VARCHAR"
                ")"))
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return

def getMostLikedRestos(): #incomplete
    list = []
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""SELECT * FROM restos LIMIT 10""")
                list = cursor.fetchall();
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return      list