from flask import render_template, abort
from common import *

from tables import restos, employees

import datetime

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>')
def main(resto_pseudo):
    resto = restos.getResto(resto_pseudo)
    if not resto:
        abort(404)

    if not resto:
        abort(404)

    employment = None

    if isLogged():
        employment = employees.getUserRestoEmployment(resto[0], getUser()[0])

    if not employees.isManager(employment) and resto[5] == False:
        return render_template('restoff.html', resto = resto);

    return render_template('resto.html', resto = resto, employment = employment);