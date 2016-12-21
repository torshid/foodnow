from flask import render_template
from common import *

import datetime

from tables import users

page = Blueprint(__name__)


@page.route('/userschoice/')
def main(user_id):
    return "HELLO AGAIN"
