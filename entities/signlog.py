from flask import render_template
from flask import request
from common import *

import datetime

page = Blueprint(__name__)

@page.route('/signup', methods = ['GET', 'POST'])
def signup():
    name = ''
    mail = ''
    password = ''
    errors = []
    if request.method == 'POST':
        if exist('name') and exist('mail') and exist('password'):
            name = request.form['name']
            mail = request.form['mail']
            password = request.form['password']
            if not validName(name):
                errors.append('Name length must be >= ' + str(namemin))
            if not validMail(mail):
                errors.append('Enter a correct mail address')
            if not validPassword(password):
                errors.append('Password length must be >= ' + str(passwordmin))
            if len(errors) == 0:
                print('db')
    return render_template('signup.html', name = name, mail = mail, password = password, errors = errors)

@page.route('/login', methods = ['GET', 'POST'])
def login():
    mail = ''
    password = ''
    remember = ''
    errors = []
    if request.method == 'POST':
        if exist('mail') and exist('password'):
            mail = request.form['mail']
            password = request.form['password']
            if exist('remember'):
                remember = ' checked'
            if validMail(mail) and validPassword(password):
                print('query')
            else:
                errors.append("Incorrect email/password")
    return render_template('login.html', mail = mail, password = password, remember = remember, errors = errors)