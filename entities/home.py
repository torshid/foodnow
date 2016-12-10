from flask import render_template
from common import *

import datetime

page = Blueprint(__name__)

@page.route('/')
def main():
    now = datetime.datetime.now()
    return render_template('home.html', current_time = now.ctime())

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS users""")
                cursor.execute("""CREATE TABLE users (id SERIAL, name VARCHAR, mail VARCHAR UNIQUE, password VARCHAR)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return