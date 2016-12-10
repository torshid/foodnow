from flask import render_template
from common import *

import datetime

page = Blueprint(__name__)

@page.route('/new-restaurant')
def new():
    return render_template('newresto.html')

@page.route('/<string:resto_pseudo>/panel')
def panel(resto_pseudo):
    return render_template('panel/home.html')

@page.route('/<string:resto_pseudo>/panel/menus')
def menus(resto_pseudo):
    return render_template('panel/menus.html')

@page.route('/<string:resto_pseudo>/panel/new-menu')
def newmenu(resto_pseudo):
    return render_template('panel/newmenu.html')

@page.route('/<string:resto_pseudo>/panel/delete-menu/<int:menu_id>')
def deletemenu(resto_pseudo, menu_id):
    return

@page.route('/<string:resto_pseudo>/panel/dishes')
def dishes(resto_pseudo):
    return render_template('panel/dishes.html')

@page.route('/<string:resto_pseudo>/panel/new-dish')
def newdish(resto_pseudo):
    return render_template('panel/newdish.html')

@page.route('/<string:resto_pseudo>/panel/delete-dish/<int:dish_id>')
def deletedish(resto_pseudo, dish_id):
    return

def reset():
    return