from flask import render_template, redirect
from flask.helpers import url_for
from common import *

import datetime

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>/panel/menus')
def menus(resto_pseudo):
    if not isLogged():
        return redirectLogin('entities.management.new')
    return render_template('panel/menus.html')

@page.route('/<string:resto_pseudo>/panel/new-menu')
def newmenu(resto_pseudo):
    if not isLogged():
        return redirectLogin('entities.management.new')
    return render_template('panel/newmenu.html')

@page.route('/<string:resto_pseudo>/panel/delete-menu/<int:menu_id>')
def deletemenu(resto_pseudo, menu_id):
    if not isLogged():
        return redirectLogin('entities.management.new')
    return

def reset():
    return