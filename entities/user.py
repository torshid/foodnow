from flask import render_template
from common import *

import datetime

from tables import users, restolikes, dishlikes
from werkzeug import redirect

page = Blueprint(__name__)

@page.route('/user/<int:user_id>/')
def main(user_id):
    if isValidUserId(user_id):
        return render_template('user.html', user_id = user_id)
    return abort(404)

@page.route('/user/<int:user_id>/settings/')
def settings(user_id):
    if isLogged():
        return render_template('settings.html', user_id = user_id)
    return render_template('home.html')

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

@page.route('/user/<int:user_id>/likeresto/<int:resto_id>/')
def likeResto(user_id, resto_id):
    from tables import restolikes
    liked = restolikes.likeResto(user_id, resto_id)
    #if liked is 0:
        #return 'Returned 0'
    #elif liked is 1:
        #return 'Returned 1'
    #else:
        #return 2
    return redirect(request.args.get('next') or request.referrer or  url_for(default))

@page.route('/user/<int:user_id>/likedish/<int:dish_id>/')
def likeDish(user_id, dish_id):
    from tables import dishlikes
    liked = dishlikes.likeDish(user_id, dish_id)
    #if liked is 0:
        #return 'Returned 0'
    #if liked is 1:
        #return 'Returned 1'
    #else:
        #return 'Returned 2'
    return redirect(request.args.get('next') or request.referrer or  url_for(default))

def reset():
    dishlikes.reset()
    restolikes.reset()
    users.reset()
    users.addUser('Yusuf Aksoy', 'yusuf@y.y', md5Password('12345'))  # id=1
    users.addUser('Moctar Sawadogo', 'moctar@m.m', md5Password('12345'))  # id=2
    users.addUser('Test User', 'test@test.com', md5Password('12345'))  # id=3
    return