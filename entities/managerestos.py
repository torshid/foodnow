from flask import render_template, redirect, abort
from flask.helpers import url_for
from common import *

from tables import restos, employees

page = Blueprint(__name__)

@page.route('/new-restaurant', methods = ['GET', 'POST'])
def new():
    if not isLogged():
        return redirectLogin('entities.managerestos.new')
    name = ''
    pseudo = ''
    mail = ''
    phone = ''
    currency = ''
    errors = []
    if request.method == 'POST':
        if exist('name') and exist('pseudo') and exist('mail') and exist('phone') and exist('currency'):
            name = request.form['name']
            pseudo = request.form['pseudo']
            mail = request.form['mail']
            phone = request.form['phone']
            currency = request.form['currency']
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
            if len(errors) == 0:
                id = restos.addResto(name, pseudo, mail, phone, currency.upper())
                employees.addEmployee(id, getUser()[0], rolemanager)
                if id == None:
                    errors.append("@name is already used")
                else:
                    return redirect(url_for('entities.panel.main', resto_pseudo = pseudo))
    return render_template('newresto.html', name = name, pseudo = pseudo, mail = mail, phone = phone, currency = currency, errors = errors)

def reset():
    restos.reset()
    employees.reset()
    restos.addResto('Kebabs Restaurant', 'kebabs', 'kebabs@foodnow.com', '532532536623')
    employees.addEmployee(1, 1, rolemanager)
    return