import datetime
import json
import os
import psycopg2 as dbapi2
import re

from flask import Flask, app
from flask import render_template

from common import *
from config import *

app = Flask(__name__)

# dynamically load all entities + register blueprints
for name in os.listdir("entities"):
    if name.endswith(".py"):
        module = name[:-3]
        globals()[module] = __import__('entities.' + module, fromlist = ['page'])
        app.register_blueprint(getattr(globals()[module], 'page'))

if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
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

def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn