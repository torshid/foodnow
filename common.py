import os
import psycopg2 as dbapi2
import hashlib
import re
import flask
from flask import Flask, session, request, redirect
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

def redirectLogin(entity):
    return redirect(url_for('entities.signlog.login', redirect_url = url_for(entity)[1:]))
