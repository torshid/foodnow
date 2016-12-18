from flask import render_template, redirect, abort
from flask.helpers import url_for
from common import *

from tables import restos, employees

import datetime

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>/panel/')
def main(resto_pseudo):
    permission = hasPanelAccess('entities.panel.main', False, resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    return render_template('panel/home.html', resto = resto)

@page.route('/<string:resto_pseudo>/panel/overview', methods = ['GET', 'POST'])
def overview(resto_pseudo):
    permission = hasPanelAccess('entities.panel.overview', resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    return render_template('panel/overview.html')

def reset():
    return