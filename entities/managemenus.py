from flask import render_template, redirect, abort, request
from flask.helpers import url_for
from common import *

from tables import restos, menus, dishes

# from flask.globals import request

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>/panel/menus', methods = ['GET', 'POST'])
def main(resto_pseudo):
    permission = hasPanelAccess('entities.managemenus.main', resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    menuslist = menus.getRestoMenus(resto[0])
    index = 0

    for menu in menuslist:
        menuslist[index] += (dishes.countMenuDishes(menu[0]),)
        index += 1

    return render_template('panel/menus.html', resto = resto, menus = menuslist)

@page.route('/<string:resto_pseudo>/panel/menus/new', methods = ['GET', 'POST'])
def new(resto_pseudo):
    permission = hasPanelAccess('entities.managemenus.new', resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    name = ''
    disposition = menus.getRestoMenuHighestDisposition(resto[0])
    if disposition:
        disposition = disposition[3] + 1
    else:
        disposition = '1'
    visible = '1'
    errors = []

    if anydata():
        if exist('name') and exist('disposition') and exist('visible'):
            name = request.form['name']
            disposition = request.form['disposition']
            visible = request.form['visible']
            if not validMenuName(name):
                errors.append('The name length must be between ' + str(menunamemin) + ' and ' + str(menunamemax))
            if not isint(disposition):
                errors.append('The disposition value must be a number')
            if not isbool(visible):
                errors.append('You must select a correct visible option')
            if len(errors) == 0:
                menus.addMenu(resto[0], name, disposition, visible)
                return redirectPanelJS('entities.managemenus.main', '<br/>' + bsalert('You successfully added the new menu ' + name, 'success'), resto_pseudo = resto_pseudo)

    return render_template('panel/newmenu.html', resto = resto, name = name, disposition = disposition, visible = visible, errors = errors)

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>', methods = ['GET', 'POST'])
def view(resto_pseudo, menu_id):
    permission = hasPanelAccess('entities.managemenus.view', resto_pseudo = resto_pseudo, menu_id = menu_id)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    menu = menus.getMenu(menu_id)
    if not menu:
        abort(404)

    if menu[1] != resto[0]:
        abort(403)

    dishs = dishes.getMenuDishes(menu[0])

    return render_template('panel/menu.html', resto = resto, menu = menu, dishes = dishs)

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/edit', methods = ['GET', 'POST'])
def edit(resto_pseudo, menu_id):
    permission = hasPanelAccess('entities.managemenus.edit', resto_pseudo = resto_pseudo, menu_id = menu_id)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    menu = menus.getMenu(menu_id)
    if not menu:
        abort(404)

    if menu[1] != resto[0]:
        abort(403)

    name = menu[2]
    disposition = menu[3]
    visible = menu[4]
    errors = []

    if anydata():
        if exist('name') and exist('disposition') and exist('visible'):
            name = request.form['name']
            disposition = request.form['disposition']
            visible = request.form['visible']
            if not validMenuName(name):
                errors.append('The name length must be between ' + str(menunamemin) + ' and ' + str(menunamemax))
            if not isint(disposition):
                errors.append('The disposition value must be a number')
            if not isbool(visible):
                errors.append('You must select a correct visible option')
            if len(errors) == 0:
                menus.updateMenu(menu[0], name, disposition, visible)
                return redirectPanelJS('entities.managemenus.main', '<br/>' + bsalert('You successfully edited the menu ' + name, 'success'), resto_pseudo = resto_pseudo)

    return render_template('panel/editmenu.html', resto = resto, menu = menu, name = name, disposition = disposition, visible = visible, errors = errors)

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/delete', methods = ['GET', 'POST'])
def delete(resto_pseudo, menu_id):
    permission = hasPanelAccess('entities.managemenus.delete', resto_pseudo = resto_pseudo, menu_id = menu_id)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    menu = menus.getMenu(menu_id)
    if not menu:
        abort(404)

    if menu[1] != resto[0]:
        abort(403)

    if dishes.countMenuDishes(menu[0]) > 0:
        return bsalert('There are dishes in the menu <a href="#" id="' + url_for('entities.managemenus.view', resto_pseudo = resto_pseudo, menu_id = menu_id) + '"><button class="btn btn-primary">' + menu[2] + '</button></a>, you need to delete them first.', 'danger')

    menus.deleteMenu(menu[0])
    return redirectPanelJS('entities.managemenus.main', '<br/>' + bsalert('You successfully deleted the menu ' + menu[2], 'info'), resto_pseudo = resto_pseudo)

def reset():
    menus.reset()
    menus.addMenu(1, 'Breakfast', 1, True)
    menus.addMenu(1, 'Kebabs', 2, True)
    menus.addMenu(1, 'Beverages', 3, True)
    return