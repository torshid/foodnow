from flask import render_template
from common import *

import datetime

page = Blueprint(__name__)

@page.route('/myprofile/<int:user_id>')
def main(user_id):
    return render_template('myprofile.html', user_id = user_id);