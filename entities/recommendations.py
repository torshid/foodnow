from flask import render_template
from common import *

import datetime
import psycopg2 as dbapi2

page = Blueprint(__name__)

@page.route('/recommendations/')
def main():
    return render_template('recommendations.html')



def reset():
    from tables import dishlikes, restolikes
    dishlikes.reset()
    restolikes.reset()
    return