import os
import psycopg2 as dbapi2
import hashlib
import flask
from jinja import *
from flask import Flask, session, request

from email.utils import parseaddr

from config import *

def Blueprint(name):  # new simple blueprint from given name
    return flask.Blueprint(name, name)

def db():  # new database connection
    return dbapi2.connect(flask.current_app.config['dsn'])

def exist(key):
    return key in request.form

def validLength(value, min, max):
    return len(value) >= min and len(value) < max

def validName(name):
    return validLength(name, namemin, namemax)

def validMail(mail):
    return validLength(parseaddr(mail)[1], mailmin, mailmax)

def validPassword(password):
    return validLength(password, passwordmin, passwordmax)

def getRestoFromPseudo(pseudo):
    return

def getUserFromPseudo(pseudo):
    return

def md5(value):
    return hashlib.md5(str(value).encode('utf-8')).hexdigest()

def md5Password(password):
    return md5('{[-' + password + '-]}')