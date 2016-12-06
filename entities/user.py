from flask import render_template
from common import *

import datetime

page = Blueprint(__name__)

@page.route('/user/<int:user_id>')
def main(user_id):
    return 'User %d' % user_id