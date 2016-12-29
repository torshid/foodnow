from flask import render_template
from common import *

import datetime

from tables import users

page = Blueprint(__name__)


@page.route('/userschoice/')
def main():
    return "HELLO AGAIN"
