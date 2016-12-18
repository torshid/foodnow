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

@page.route('/<string:resto_pseudo>/panel/settings', methods = ['GET', 'POST'])
def settings(resto_pseudo):
    permission = hasPanelAccess('entities.panel.settings', resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    return render_template('panel/settings.html')

@page.route('/<string:resto_pseudo>/panel/reviews', methods = ['GET', 'POST'])
def reviews(resto_pseudo):
    permission = hasPanelAccess('entities.panel.reviews', resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    return render_template('panel/reviews.html')

@page.route('/<string:resto_pseudo>/panel/statistics', methods = ['GET', 'POST'])
def statistics(resto_pseudo):
    permission = hasPanelAccess('entities.panel.statistics', resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    return render_template('panel/statistics.html')

def reset():
    return