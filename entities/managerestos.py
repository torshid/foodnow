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
    description = ''
    errors = []
    if request.method == 'POST':
        if exist('name') and exist('pseudo') and exist('mail') and exist('phone') and exist('currency') and exist('description'):
            name = request.form['name']
            pseudo = request.form['pseudo']
            mail = request.form['mail']
            phone = request.form['phone']
            currency = request.form['currency']
            description = request.form['description']
            if not validRestoName(name):
                errors.append('Name length must be >= ' + str(restonamemin))
            if not validRestoPseudo(pseudo):
                errors.append('@name length must be >= ' + str(restopseudomin) + ' and contain only letters and digits')
            if not validMail(mail):
                errors.append('Enter a correct mail address')
            if not validPhone(phone):
                errors.append('Enter a correct phone number')
            if not validCurrency(currency):
                errors.append('Enter a correct currency (TRY, AED, USD, ...)')
            if not validDescription(description):
                errors.append('Description length must be <= ' + str(restodescriptionmax))
            if len(errors) == 0:
                id = restos.addResto(name, pseudo, mail, phone, currency.upper(), description)
                employees.addEmployee(id, getUser()[0], rolemanager)
                if id == None:
                    errors.append("@name is already used")
                else:
                    return redirect(url_for('entities.panel.main', resto_pseudo = pseudo))
    return render_template('newresto.html', name = name, pseudo = pseudo, mail = mail, phone = phone, currency = currency, description = description, errors = errors)

def reset():
    restos.reset()
    employees.reset()
    restos.addResto('Kebabs Restaurant', 'kebabs', 'kebabs@foodnow.com', '5325325366', 'TRY', 'The best kebabs of Turkey here!')
    employees.addEmployee(1, 1, rolemanager)
    return