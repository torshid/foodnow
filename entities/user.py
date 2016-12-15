from flask import render_template
from common import *

import datetime

from tables import users

page = Blueprint(__name__)

@page.route('/user/<int:user_id>')
def main(user_id):
    return render_template('user.html', user_id = user_id)

def updateProfile(userId):
    with db() as connection:
        with connection.cursor() as cursor:
            query = """UPDATE users
                            SET"""
            try:
                cursor.execute(query);
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return

def reset():
    users.reset()
    return