from flask import render_template, abort
from common import *

from tables import restos

import datetime

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>')
def main(resto_pseudo):
    resto = restos.getResto(resto_pseudo)
    if not resto:
        abort(404)
    return render_template('resto.html', resto = resto);