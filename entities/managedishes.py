from flask import render_template, redirect
from flask.helpers import url_for
from common import *

import datetime

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>/panel/dishes')
def dishes(resto_pseudo):
    if not isLogged():
        return redirectLogin('entities.management.new')
    return render_template('panel/dishes.html')

@page.route('/<string:resto_pseudo>/panel/new-dish')
def newdish(resto_pseudo):
    if not isLogged():
        return redirectLogin('entities.management.new')
    return render_template('panel/newdish.html')

@page.route('/<string:resto_pseudo>/panel/delete-dish/<int:dish_id>')
def deletedish(resto_pseudo, dish_id):
    if not isLogged():
        return redirectLogin('entities.management.new')
    return

def reset():
    return