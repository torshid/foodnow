import os
import psycopg2 as dbapi2
import hashlib
import re
import flask
from flask import Flask, session, request, redirect, render_template, abort
from flask.helpers import url_for

from email.utils import parseaddr

from jinja import *
from config import *

def Blueprint(name):  # new simple blueprint from given name
    return flask.Blueprint(name, name)

def db():  # new database connection
    return dbapi2.connect(flask.current_app.config['dsn'])

def exist(key):
    return key in request.form

def anydata():
    return len(request.form) > 0

def validLength(value, min, max):
    value = value.strip()
    return len(value) >= min and len(value) <= max

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

def validMenuName(name):
    return validLength(name, menunamemin, menunamemax)

def validCurrency(currency):
    return validLength(currency, 3, 3)

def validWarnmsg(warnmsg):
    return validLength(warnmsg, 0, restowarnmsgmax)

def validDishName(name):
    return validLength(name, dishnamemin, dishnamemax)

def validPhone(phone):
    phone = phone.strip()
    result = re.match("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", phone)
    if not result:
        return False
    return len(result.group(0)) == len(phone)

def isbool(s):
    s = s.lower()
    return s == '1' or s == 1 or s == '0' or s == 0 or s == 'true' or s == 'false'

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def md5(value):
    return hashlib.md5(str(value).encode('utf-8')).hexdigest()

def md5Password(password):
    return md5('{[-' + password + '-]}')

def hasPanelAccess(entity, onlypost = True, **data):
    if not isLogged():
        return redirectLogin(entity, **data)
    if onlypost and request.method == 'GET':
        return redirectPanel(entity, **data)

    from tables import restos, employees

    resto = restos.getResto(data['resto_pseudo'])
    if not resto:
        abort(404)

    employment = employees.getUserRestoEmployment(resto[0], getUser()[0])

    if not employees.isManager(employment):
        abort(403)

    return (resto, employment)

def redirectLogin(entity, **data):
    return redirect(url_for('entities.signlog.login', redirect_url = url_for(entity, **data)[1:]))

def redirectPanel(entity, **data):
    return redirect(url_for('entities.panel.main', resto_pseudo = data['resto_pseudo']) + "#" + url_for(entity, **data).replace('/' + data['resto_pseudo'] + '/panel/', ''))

def redirectPanelJS(entity, message = None, **data):
    return "<script>loadPage('" + url_for(entity, **data).replace('/' + data['resto_pseudo'] + '/panel/', '') + "', true, null" + ((", '" + message + "'") if message else ', null') + ");</script>"

def bsalert(message, type = None):
    if not type:
        type = 'info'
    return '<div class="alert alert-' + type + ' alert-dismissable fade in"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>' + message + '</div>'

def select(table, all, dict = None, extra = None):
    result = None
    if not extra:
        extra = ''
    with db() as connection:
        with connection.cursor() as cursor:
            if dict:
                placeholders = ' AND '.join(['%s = %s' % (key, '%s') for (key, value) in dict.items()])
                query = "SELECT * FROM %s WHERE %s %s" % (table, placeholders, extra)
            else:
                query = "SELECT * FROM %s %s" % (table, extra)
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

def selectone(table, dict = None, extra = None):
    return select(table, False, dict, extra)

def selectall(table, dict = None, extra = None):
    return select(table, True, dict, extra)

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

def update(table, dict, extra = None):
    result = False
    if not extra:
        extra = [{}]
    with db() as connection:
        with connection.cursor() as cursor:
            placeholders1 = ', '.join(['%s = %s' % (key, '%s') for (key, value) in dict.items()])
            placeholders2 = '1=1'
            if len(extra) > 0:
                  placeholders2 = ' AND '.join(['%s = %s' % (key, '%s') for (key, value) in extra.items()])
            query = "UPDATE %s SET %s WHERE %s" % (table, placeholders1, placeholders2)
            try:
                cursor.execute(query, (list(dict.values()) + list(extra.values())))
                result = True
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return result






