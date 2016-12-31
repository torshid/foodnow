from flask import render_template, redirect
from flask.helpers import url_for

from common import *

from tables import menus, dishes
from flask.globals import request

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>/panel/dishes', methods = ['GET', 'POST'])
def main(resto_pseudo):
    permission = hasPanelAccess('entities.managedishes.dishes', resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    return render_template('panel/dishes.html')

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/new', methods = ['GET', 'POST'])
def newdish(resto_pseudo, menu_id):
    permission = hasPanelAccess('entities.managedishes.newdish', resto_pseudo = resto_pseudo, menu_id = menu_id)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    menu = menus.getMenu(menu_id)
    if not menu:
        abort(404)

    if menu[1] != resto[0]:
        abort(403)

    name = ''
    price = ''
    disposition = dishes.getMenuDishesHighestDisposition(menu[0])
    if disposition:
        disposition = disposition[3] + 1
    else:
        disposition = '1'
    visible = '1'
    errors = []

    if anydata():
        if exist('name') and exist('price') and exist('disposition') and exist('visible'):
            name = request.form['name']
            price = request.form['price']
            disposition = request.form['disposition']
            visible = request.form['visible']
            if not validDishName(name):
                errors.append('The name length must be between ' + str(dishnamemin) + ' and ' + str(dishnamemax))
            if not isfloat(price):
                errors.append('The price value must be a (real) number')
            if not isint(disposition):
                errors.append('The disposition value must be a number')
            if len(errors) == 0:
                dishes.addDish(menu[0], name, price, disposition, visible)
                return redirectPanelJS('entities.managemenus.view', '<br/>' + bsalert('You successfully added the new dish ' + name, 'success'), resto_pseudo = resto_pseudo, menu_id = menu_id)

    return render_template('panel/newdish.html', menu = menu, name = name, price = price, disposition = disposition, visible = visible, errors = errors)

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/<int:dish_id>/delete', methods = ['GET', 'POST'])
def deletedish(resto_pseudo, menu_id, dish_id):
    permission = hasPanelAccess('entities.managedishes.deletedish', resto_pseudo = resto_pseudo, menu_id = menu_id, dish_id = dish_id)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    menu = menus.getMenu(menu_id)
    if not menu:
        abort(404)

    if menu[1] != resto[0]:
        abort(403)

    dish = dishes.getDish(dish_id)
    if not dish:
        abort(404)

    if dish[1] != menu[0]:
        abort(403)

    dishes.deleteDish(dish[0])
    return redirectPanelJS('entities.managemenus.view', '<br/>' + bsalert('You successfully deleted the dish ' + dish[2], 'info'), resto_pseudo = resto_pseudo, menu_id = menu_id)

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/<int:dish_id>', methods = ['GET', 'POST'])
def dish(resto_pseudo, menu_id, dish_id):
    permission = hasPanelAccess('entities.managedishes.dish', resto_pseudo = resto_pseudo, menu_id = menu_id, dish_id = dish_id)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    menu = menus.getMenu(menu_id)
    if not menu:
        abort(404)

    if menu[1] != resto[0]:
        abort(403)

    dish = dishes.getDish(dish_id)
    if not dish:
        abort(404)

    if dish[1] != menu[0]:
        abort(403)

    return render_template('panel/dish.html', menu = menu, dish = dish)

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/<int:dish_id>/edit', methods = ['GET', 'POST'])
def editdish(resto_pseudo, menu_id, dish_id):
    permission = hasPanelAccess('entities.managedishes.editdish', resto_pseudo = resto_pseudo, menu_id = menu_id, dish_id = dish_id)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    menu = menus.getMenu(menu_id)
    if not menu:
        abort(404)

    if menu[1] != resto[0]:
        abort(403)

    dish = dishes.getDish(dish_id)
    if not dish:
        abort(404)

    if dish[1] != menu[0]:
        abort(403)

    name = dish[2]
    price = dish[3]
    disposition = dish[4]
    visible = [5]
    errors = []

    if anydata():
        if exist('name') and exist('price') and exist('disposition') and exist('visible'):
            name = request.form['name']
            price = request.form['price']
            disposition = request.form['disposition']
            visible = request.form['visible']
            if not validDishName(name):
                errors.append('The name length must be between ' + str(dishnamemin) + ' and ' + str(dishnamemax))
            if not isfloat(price):
                errors.append('The price value must be a (real) number')
            if not isint(disposition):
                errors.append('The disposition value must be a number')
            if len(errors) == 0:
                dishes.updateDish(dish[0], name, price, disposition, visible)
                return redirectPanelJS('entities.managemenus.view', '<br/>' + bsalert('You successfully edited the dish ' + name, 'success'), resto_pseudo = resto_pseudo, menu_id = menu_id)

    return render_template('panel/editdish.html', menu = menu, dish = dish, name = name, price = price, disposition = disposition, visible = visible, errors = errors)

def reset():
    dishes.reset()
    return