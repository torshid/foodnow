from flask import render_template
from common import *

import datetime

from tables import users

page = Blueprint(__name__)


@page.route('/foodforum/')
def main():
    return "HELLO"
