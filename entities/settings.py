from flask import render_template
from common import *

import datetime

page = Blueprint(__name__)

@page.route('/settings/')
def main(user_id):
    return render_template('settings.html')