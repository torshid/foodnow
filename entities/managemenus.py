from flask import render_template, redirect
from flask.helpers import url_for
from common import *

from tables import restos

import datetime

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>/panel/menus', methods = ['GET', 'POST'])
def main(resto_pseudo):
    if not isLogged():
        return redirectLogin('entities.managemenus.main', resto_pseudo = resto_pseudo)
    if request.method == 'GET':
        return redirectPanel('entities.managemenus.main', resto_pseudo = resto_pseudo)

    resto = restos.getResto(resto_pseudo)
    if not resto:
        abort(404)
    return render_template('panel/menus.html')

@page.route('/<string:resto_pseudo>/panel/new-menu')
def newmenu(resto_pseudo):
    if not isLogged():
        return redirectLogin('entities.managerestos.new')
    return render_template('panel/newmenu.html')

@page.route('/<string:resto_pseudo>/panel/delete-menu/<int:menu_id>')
def deletemenu(resto_pseudo, menu_id):
    if not isLogged():
        return redirectLogin('entities.managerestos.delete')
    return

def reset():
    return