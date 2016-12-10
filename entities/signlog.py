from flask import render_template, request, redirect, make_response, Markup
from flask.helpers import url_for

from common import *

from tables import users

import datetime

page = Blueprint(__name__)

@page.route('/signup', methods = ['GET', 'POST'])
def signup():
    if isLogged():
        return redirect(url_for('entities.home.main'))
    name = ''
    mail = ''
    password = ''
    errors = []
    if request.method == 'POST':
        if exist('name') and exist('mail') and exist('password'):
            name = request.form['name']
            mail = request.form['mail']
            password = request.form['password']
            hashed = None
            if not validName(name):
                errors.append('Name length must be >= ' + str(namemin))
            if not validMail(mail):
                errors.append('Enter a correct mail address')
            if not validPassword(password):
                errors.append('Password length must be >= ' + str(passwordmin))
            else:
                hashed = md5Password(password)
            if len(errors) == 0:
                id = users.addUser(name, mail, hashed)
                if id == None:
                    errors.append("Mail address is already used")
                else:
                    session['mail'] = mail
                    session['password'] = hashed
                    response = make_response(redirect(url_for('entities.home.main')))
                    expire = datetime.datetime.now() + datetime.timedelta(days = 120)
                    response.set_cookie('mail', mail, expires = expire)
                    response.set_cookie('password', hashed, expires = expire)
                    return response
    return render_template('signup.html', name = name, mail = mail, password = password, errors = errors)

@page.route('/login', defaults = {'redirect_url': None}, methods = ['GET', 'POST'])
@page.route('/login/<path:redirect_url>', methods = ['GET', 'POST'])
def login(redirect_url):
    if isLogged():
        return redirect(url_for('entities.home.main'))
    mail = ''
    password = ''
    remember = ''
    errors = []
    if redirect_url:
        errors.append('Login needed to access page ' + Markup('<i><b>') + redirect_url + Markup('</b></i>'))
    if request.method == 'POST':
        if exist('mail') and exist('password'):
            mail = request.form['mail']
            password = request.form['password']
            if len(mail) > 0 and len(password) > 0:
                hashed = None
                if exist('present'):
                    if exist('remember'):
                        remember = 'checked'
                else:
                    remember = ' checked'
                if validMail(mail) and validPassword(password):
                    hashed = md5Password(password)
                    user = users.getUser(mail, hashed)
                    if user:
                        session['mail'] = mail
                        session['password'] = hashed
                        redirectpage = url_for('entities.home.main')
                        if redirect_url:
                            redirectpage = redirect_url
                        response = make_response(redirect(redirectpage))
                        if remember != '':
                            expire = datetime.datetime.now() + datetime.timedelta(days = 120)
                            response.set_cookie('mail', mail, expires = expire)
                            response.set_cookie('password', hashed, expires = expire)
                        return response
                    else:
                        errors.append("Incorrect email/password")
                else:
                    errors.append("Incorrect email/password")
    return render_template('login.html', mail = mail, password = password, remember = remember, errors = errors, redirect_url = redirect_url)

@page.route('/logout')
def logout():
    response = make_response(redirect(url_for('entities.home.main')))
    response.set_cookie('mail', '', expires = 0)
    response.set_cookie('password', '', expires = 0)
    if 'mail' in session: del session['mail']
    if 'password' in session: del session['password']
    if 'user' in session: del session['user']
    return response