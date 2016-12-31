from flask import render_template, redirect
from flask.helpers import url_for

from common import *

from tables import menus, dishes

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>/panel/dishes')
def dishes(resto_pseudo):
    permission = hasPanelAccess('entities.managedishes.dishes', resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    return render_template('panel/dishes.html')

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/new')
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

    return render_template('panel/newdish.html')

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/<int:dish_id>/delete')
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

    return

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes')
def menudishes(resto_pseudo, menu_id):
    permission = hasPanelAccess('entities.managedishes.menudishes', resto_pseudo = resto_pseudo, menu_id = menu_id)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    menu = menus.getMenu(menu_id)
    if not menu:
        abort(404)

    if menu[1] != resto[0]:
        abort(403)

    return render_template('panel/menudishes.html')

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/<int:dish_id>')
def dish(resto_pseudo, menu_id):
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

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/<int:dish_id>/edit')
def editdish(resto_pseudo, menu_id):
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

    return render_template('panel/editdish.html')

def reset():
    dishes.reset()
    return