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
    return render_template('signup.html', name = name, mail = mail, password = password, errors = errors)

@page.route('/login', methods = ['GET', 'POST'])
def login():
    mail = ''
    password = ''
    remember = ''
    errors = []
    errors.append('hello')
    if request.method == 'POST':
        if exist('mail') and exist('password'):
            mail = request.form['mail']
            password = request.form['password']
            if exist('remember'):
                remember = ' checked'
    return render_template('login.html', mail = mail, password = password, remember = remember, errors = errors)