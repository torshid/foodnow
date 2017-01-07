from flask import render_template
from common import *

from tables import restos

page = Blueprint(__name__)

@page.route('/')
def main():
    restolist = restos.getLastRestos()
    return render_template('home.html', restos = restolist)