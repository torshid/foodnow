from flask import render_template, redirect, abort
from flask.helpers import url_for
from common import *

from tables import restos

import datetime

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>/panel/')
def main(resto_pseudo):
    if not isLogged():
        return redirectLogin('entities.panel.main', resto_pseudo = resto_pseudo)
    resto = restos.getResto(resto_pseudo)
    if not resto:
        abort(404)
    return render_template('panel/home.html', name = resto[1])

@page.route('/<string:resto_pseudo>/panel/overview', methods = ['GET', 'POST'])
def overview(resto_pseudo):
    if not isLogged():
        return redirectLogin('entities.panel.overview', resto_pseudo = resto_pseudo)
    if request.method == 'GET':
        return redirectPanel('entities.panel.overview', resto_pseudo = resto_pseudo)

    resto = restos.getResto(resto_pseudo)
    if not resto:
        abort(404)
    return render_template('panel/overview.html')

def reset():
    return