from flask import render_template
from common import *

import datetime

from tables import users

page = Blueprint(__name__)

@page.route('/user/<int:user_id>')
def main(user_id):
    return render_template('user.html', user_id = user_id)

def updateProfile(userId, name = None, email = None, password = None):
    if (isLogged()):
        args = [name, email, password]
        settings = []
        for i in range(3):
            if args[i]:
                if i is 2:
                    settings.append(md5Password(args[i]))
                else:
                    settings.append(args[i])
        with db() as connection:
            with connection.cursor() as cursor:

                try:
                    update(userId, settings);
                except dbapi2.Error:
                    connection.rollback()
                else:
                    connection.commit()
    return

def reset():
    users.reset()
    users.addUser('Yusuf Aksoy', 'yusuf@y.y', md5Password('12345'))  # id=1
    users.addUser('Moctar Sawadogo', 'moctar@m.m', md5Password('12345'))  # id=2
    return