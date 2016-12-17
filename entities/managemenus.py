from flask import render_template, redirect, abort
from flask.helpers import url_for
from common import *

from tables import restos, menus

import datetime
from flask.globals import request

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

    return render_template('panel/menus.html', menus = menus.getRestoMenus(resto[0]))

@page.route('/<string:resto_pseudo>/panel/new-menu', methods = ['GET', 'POST'])
def newmenu(resto_pseudo):
    if not isLogged():
        return redirectLogin('entities.managemenus.main', resto_pseudo = resto_pseudo)
    if request.method == 'GET':
        return redirectPanel('entities.managemenus.newmenu', resto_pseudo = resto_pseudo)

    if anydata():
        return redirectPanelJS('entities.managemenus.main', '<br/>' + bsalert(request.form['content']), resto_pseudo = resto_pseudo)

    return render_template('panel/newmenu.html')

@page.route('/<string:resto_pseudo>/panel/delete-menu/<int:menu_id>', methods = ['GET', 'POST'])
def deletemenu(resto_pseudo, menu_id):
    if not isLogged():
        return redirectLogin('entities.managemenus.main', resto_pseudo = resto_pseudo)

    return

def reset():
    menus.reset()
    return