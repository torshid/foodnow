from flask import render_template
from common import *

import datetime

page = Blueprint(__name__)

@page.route('/')
def main():
    with db() as connection:  # just a test
        now = datetime.datetime.now()
    return render_template('home.html', current_time = now.ctime())