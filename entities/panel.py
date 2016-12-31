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

    name = resto[1]
    pseudo = resto[2]
    mail = resto[3]
    phone = resto[4]
    accessible = resto[5]
    warnmsg = resto[6]
    currency = resto[7]
    description = resto[8]
    errors = []

    if request.method == 'POST':
        if exist('name') and exist('pseudo') and exist('mail') and exist('phone') and exist('accessible') and exist('warnmsg') and exist('currency') and exist('description'):
            name = request.form['name']
            pseudo = request.form['pseudo']
            mail = request.form['mail']
            phone = request.form['phone']
            accessible = request.form['accessible']
            warnmsg = request.form['warnmsg']
            currency = request.form['currency']
            description = request.form['description']
            if not validRestoName(name):
                errors.append('Name length must be >= ' + str(restonamemin))
            if not validRestoPseudo(pseudo):
                errors.append('@name length must be >= ' + str(restopseudomin))
            if not validMail(mail):
                errors.append('Enter a correct mail address')
            if not validPhone(phone):
                errors.append('Enter a correct phone number')
            if not validCurrency(currency):
                errors.append('Enter a correct currency (TRY, AED, USD, ...)')
            if not validDescription(description):
                errors.append('Description length must be <= ' + str(restodescriptionmax))
            if not isbool(accessible):
                errors.append('You must select a correct accessible option')
            if not validWarnmsg(warnmsg):
                errors.append('The disabled message length must be <= ' + str(restowarnmsgmax))
            if len(errors) == 0:
                updated = restos.updateResto(resto[0], name, pseudo, mail, phone, accessible, warnmsg, currency.upper(), description)
                if not updated:
                    errors.append("@name is already used")
                else:
                    return redirectPanelJS('entities.panel.settings', '<br/>' + bsalert('You successfully edited the settings', 'success'), resto_pseudo = resto_pseudo)

    return render_template('panel/settings.html', resto = resto, name = name, pseudo = pseudo, mail = mail, phone = phone, accessible = accessible, warnmsg = warnmsg, currency = currency, description = description, errors = errors)

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