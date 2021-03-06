import datetime
import json
import os
import psycopg2 as dbapi2
import re

from werkzeug.exceptions import NotFound, Forbidden
from flask import Flask, app, render_template

from common import *
from config import *
import jinja

app = Flask(__name__)

# jinja-python functions
@app.context_processor
def processor():
    functions = {}
    for function in jinja.__dict__.values():
        if callable(function):
          functions[function.__name__] = function
    return functions

# dynamically load all entities + register blueprints
for name in os.listdir("entities"):
    if name.endswith(".py"):
        module = name[:-3]
        globals()[module] = __import__('entities.' + module, fromlist = ['page'])
        app.register_blueprint(getattr(globals()[module], 'page'))

@app.errorhandler(NotFound)
def error(e):
    return render_template('errors/' + str(e.code) + '.html'), e.code

@app.errorhandler(Forbidden)
def error(e):
    return render_template('errors/' + str(e.code) + '.html'), e.code

def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

if __name__ == '__main__':
    app.secret_key = flaskkey
    VCAP_APP_PORT = os.getenv('PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = "user='" + dbuser + "' password='" + dbpass + "' host='localhost' port=5432 dbname='" + dbname + "'"

    app.run(host = '0.0.0.0', port = port, debug = debug)