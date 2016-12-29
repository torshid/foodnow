from flask import render_template
from common import *

import datetime

from tables import users

page = Blueprint(__name__)

@page.route('/reviews/<int:user_id>')
def main(user_id):
    return "HELLO"

def reset():
    users.reset()
    return