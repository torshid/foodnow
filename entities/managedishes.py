from flask import render_template, redirect
from flask.helpers import url_for

from common import *

from tables import menus, dishes
from flask.globals import request

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes', methods = ['GET', 'POST'])
def main(resto_pseudo, menu_id):
    return redirectPanel('entities.managemenus.view', resto_pseudo = resto_pseudo, menu_id = menu_id)

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/new', methods = ['GET', 'POST'])
def new(resto_pseudo, menu_id):
    permission = hasPanelAccess('entities.managedishes.new', resto_pseudo = resto_pseudo, menu_id = menu_id)
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
        disposition = disposition[4] + 1
    else:
        disposition = '1'
    visible = '1'
    description = ''
    errors = []

    if anydata():
        if exist('name') and exist('price') and exist('disposition') and exist('visible') and exist('description'):
            name = request.form['name']
            price = request.form['price']
            disposition = request.form['disposition']
            visible = request.form['visible']
            description = request.form['description']
            if not validDishName(name):
                errors.append('The name length must be between ' + str(dishnamemin) + ' and ' + str(dishnamemax))
            if not validDishDescription(description):
                errors.append('The description length must be <=' + str(dishdescriptionmax))
            if not isfloat(price):
                errors.append('The price value must be a (real) number')
            if not isint(disposition):
                errors.append('The disposition value must be a number')
            if not isbool(visible):
                errors.append('You must select a correct visible option')
            if len(errors) == 0:
                id = dishes.addDish(menu[0], name, price, disposition, visible, description)
                pctfile = dishespctpath + str(id) + '.png'
                if checkUpload(pctextensions, pctfile):
                    resizePicture(pctfile, pctfile, dishpctsize)
                    resizePicture(pctfile, dishesthumbspath + str(id) + '.png', dishthumbsize)
                return redirectPanelJS('entities.managemenus.view', '<br/>' + bsalert('You successfully added the new dish ' + name, 'success'), resto_pseudo = resto_pseudo, menu_id = menu_id)

    return render_template('panel/newdish.html', resto = resto, menu = menu, name = name, price = price, disposition = disposition, visible = visible, description = description, errors = errors)

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/<int:dish_id>/delete', methods = ['GET', 'POST'])
def delete(resto_pseudo, menu_id, dish_id):
    permission = hasPanelAccess('entities.managedishes.delete', resto_pseudo = resto_pseudo, menu_id = menu_id, dish_id = dish_id)
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
def view(resto_pseudo, menu_id, dish_id):
    permission = hasPanelAccess('entities.managedishes.view', resto_pseudo = resto_pseudo, menu_id = menu_id, dish_id = dish_id)
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

    return render_template('panel/dish.html', resto = resto, menu = menu, dish = dish)

@page.route('/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/<int:dish_id>/edit', methods = ['GET', 'POST'])
def edit(resto_pseudo, menu_id, dish_id):
    permission = hasPanelAccess('entities.managedishes.edit', resto_pseudo = resto_pseudo, menu_id = menu_id, dish_id = dish_id)
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

    allmenus = menus.getRestoMenus(resto[0])

    menuid = dish[1]
    name = dish[2]
    price = dish[3]
    disposition = dish[4]
    visible = dish[5]
    description = dish[7]
    errors = []

    if anydata():
        if exist('menu') and exist('name') and exist('price') and exist('disposition') and exist('visible') and exist('description'):
            menuid = request.form['menu']
            name = request.form['name']
            price = request.form['price']
            disposition = request.form['disposition']
            visible = request.form['visible']
            description = request.form['description']
            newmenu = menus.getMenu(menuid)
            if not newmenu or newmenu[1] != resto[0]:
                errors.append('You have to select a correct menu')
            if not validDishName(name):
                errors.append('The name length must be between ' + str(dishnamemin) + ' and ' + str(dishnamemax))
            if not validDishDescription(description):
                errors.append('The description length must be <=' + str(dishdescriptionmax))
            if not isfloat(price):
                errors.append('The price value must be a (real) number')
            if not isint(disposition):
                errors.append('The disposition value must be a number')
            if not isbool(visible):
                errors.append('You must select a correct visible option')
            if len(errors) == 0:
                pctfile = dishespctpath + str(dish[0]) + '.png'
                dishes.updateDish(dish[0], menuid, name, price, disposition, visible, description)
                if checkUpload(pctextensions, pctfile):
                    resizePicture(pctfile, pctfile, dishpctsize)
                    resizePicture(pctfile, dishesthumbspath + str(dish[0]) + '.png', dishthumbsize)

                return redirectPanelJS('entities.managemenus.view', '<br/>' + bsalert('You successfully edited the dish ' + name, 'success'), resto_pseudo = resto_pseudo, menu_id = newmenu[0])

    return render_template('panel/editdish.html', resto = resto, menu = menu, menus = allmenus, menuid = menuid, dish = dish, name = name, price = price, disposition = disposition, visible = visible, description = description, errors = errors)

def reset():
    dishes.reset()
    dishes.addDish(1, 'Omelette', 10, 1, True, 'Simply eggs!')
    dishes.addDish(1, 'Croissant', 6, 2, True, 'Original kebab')
    dishes.addDish(2, 'Adana Kebab', 45, 1, True, 'With some extras')
    dishes.addDish(2, 'Chicken Kebab', 29, 2, True, 'Look at that, yummy')
    dishes.addDish(2, 'Sandwich', 15, 3, True, 'The best in da world')
    dishes.addDish(3, 'Cola', 4, 1, True, 'A must try, or maybe not')
    dishes.addDish(3, 'Tea', 2, 1, True, 'Traditional Turkish drink')
    return