from flask import render_template, redirect, abort
from flask.helpers import url_for
from common import *

from tables import restos, employees

import datetime

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>/panel/orders', methods = ['GET', 'POST'])
def main(resto_pseudo):
    permission = hasPanelAccess('entities.orders.main', False, resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    return render_template('panel/orders.html', resto = resto)