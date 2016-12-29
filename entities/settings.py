from flask import render_template
from common import *

import datetime

page = Blueprint(__name__)

@page.route('/settings/')
def main():
    return render_template('settings.html')
