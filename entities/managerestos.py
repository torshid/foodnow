from flask import render_template, redirect, abort
from flask.helpers import url_for
from common import *

from tables import restos

import datetime

page = Blueprint(__name__)

@page.route('/new-restaurant', methods = ['GET', 'POST'])
def new():
    if not isLogged():
        return redirectLogin('entities.managerestos.new')
    name = ''
    pseudo = ''
    mail = ''
    phone = ''
    errors = []
    if request.method == 'POST':
        if exist('name') and exist('pseudo') and exist('mail') and exist('phone'):
            name = request.form['name']
            pseudo = request.form['pseudo']
            mail = request.form['mail']
            phone = request.form['phone']
            if not validRestoName(name):
                errors.append('Name length must be >= ' + str(restonamemin))
            if not validRestoPseudo(pseudo):
                errors.append('@name length must be >= ' + str(restopseudomin))
            if not validMail(mail):
                errors.append('Enter a correct mail address')
            if not validPhone(phone):
                errors.append('Enter a correct phone number')
            if len(errors) == 0:
                id = restos.addResto(name, pseudo, mail, phone)
                if id == None:
                    errors.append("@name is already used")
                else:
                    return redirect(url_for('entities.managerestos.panel', resto_pseudo = pseudo))
    return render_template('newresto.html', name = name, pseudo = pseudo, mail = mail, phone = phone, errors = errors)

@page.route('/<string:resto_pseudo>/panel')
def panel(resto_pseudo):
    if not isLogged():
        return redirectLogin('entities.management.new')
    resto = restos.getResto(resto_pseudo)
    if not resto:
        abort(404)
    return render_template('panel/home.html', resto = resto)

def reset():
    with db() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""DROP TABLE IF EXISTS restos""")
                cursor.execute("""CREATE TABLE restos (id SERIAL, name VARCHAR, pseudo VARCHAR UNIQUE, mail VARCHAR, phone VARCHAR)""")
            except dbapi2.Error:
                connection.rollback()
            else:
                connection.commit()
    return