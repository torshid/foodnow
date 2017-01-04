from flask import render_template, send_file
from common import *

page = Blueprint(__name__)

@page.route('/images/dishes/<int:dish_id>.png')
def dishimage(dish_id):
    filename = dishespctpath + str(dish_id) + '.png'
    # if not fileExists(filename):
    #    abort(403)
    return send_file(filename, mimetype = 'image/png')