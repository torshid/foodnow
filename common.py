import os
import psycopg2 as dbapi2
import flask
from flask import request

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