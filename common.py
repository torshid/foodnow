import os
import psycopg2 as dbapi2
import hashlib
import re
import flask
from flask import Flask, session, request, redirect, render_template
from flask.helpers import url_for
from jinja import *

from email.utils import parseaddr

from config import *

def Blueprint(name):  # new simple blueprint from given name
    return flask.Blueprint(name, name)

def db():  # new database connection
    return dbapi2.connect(flask.current_app.config['dsn'])

def exist(key):
    return key in request.form

def validLength(value, min, max):
    value = value.strip()
    return len(value) >= min and len(value) < max

def validName(name):
    return validLength(name, namemin, namemax)

def validMail(mail):
    return validLength(parseaddr(mail)[1], mailmin, mailmax)

def validPassword(password):
    return validLength(password, passwordmin, passwordmax)

def validRestoName(name):
    return validLength(name, restonamemin, restonamemax)

def validRestoPseudo(pseudo):
    return validLength(pseudo, restopseudomin, restopseudomax)

def validPhone(phone):
    phone = phone.strip()
    result = re.match("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", phone)
    if not result:
        return False
    return len(result.group(0)) == len(phone)

def md5(value):
    return hashlib.md5(str(value).encode('utf-8')).hexdigest()

def md5Password(password):
    return md5('{[-' + password + '-]}')

def redirectLogin(entity, **data):
    return redirect(url_for('entities.signlog.login', redirect_url = url_for(entity, **data)[1:]))

def redirectPanel(entity, **data):
    return redirect(url_for('entities.panel.main', resto_pseudo = data['resto_pseudo']) + "#" + url_for(entity, **data).replace('/' + data['resto_pseudo'] + '/panel/', ''))

def select(table, all, dict = None):
    result = None
    with db() as connection:
        with connection.cursor() as cursor:
            if dict:
                placeholders = ' AND '.join(['%s = %s' % (key, '%s') for (key, value) in dict.items()])
                query = "SELECT * FROM %s WHERE %s" % (table, placeholders)
            else:
                query = "SELECT * FROM %s" % (table)
            try:
                if dict:
                    cursor.execute(query, list(dict.values()))
                else:
                    cursor.execute(query)
                if all:
                    result = cursor.fetchall()
                else:
                    result = cursor.fetchone()
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return result

def selectone(table, dict = None):
    return select(table, False, dict)

def selectall(table, dict = None):
    return select(table, True, dict)

def delete(table, dict):
    result = None
    with db() as connection:
        with connection.cursor() as cursor:
            placeholders = ' AND '.join(['%s = %s' % (key, '%s') for (key, value) in dict.items()])
            query = "DELETE FROM %s WHERE %s" % (table, placeholders)
            try:
                cursor.execute(query, list(dict.values()))
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
            print(cursor.query)
    return result

def insert(table, dict, simple = None):
    placeholders = ', '.join(['%s'] * len(dict))
    columns = ', '.join(dict.keys())
    query = "INSERT INTO %s (%s) VALUES (%s)" % (table, columns, placeholders)
    result = False
    if not simple:
        query += " RETURNING id"
        result = None
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, list(dict.values()))
                if not simple:
                    result = cursor.fetchone()[0]
                else:
                    result = True
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return result








